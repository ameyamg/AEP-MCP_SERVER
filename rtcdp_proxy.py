"""
Stdio → HTTPS proxy for Adobe's official Real-Time CDP MCP server.

The upstream server uses the MCP streamable-HTTP transport (POST-based).
Auth headers (Bearer token, x-api-key, x-gw-ims-org-id) are sourced from
the active org profile in orgs.json, so switch_org_profile also switches
which org the RT-CDP tools run against.

This is a standalone entrypoint — it is NOT imported by server.py.
Configure RTCDP_MCP_URL in .env (default: https://rtcdp-mcp.adobe.io/mcp).

Add to .claude/mcp_servers.json:
  {
    "rtcdp": {
      "command": "python",
      "args": ["/path/to/aep-mcp-server/rtcdp_proxy.py"]
    }
  }
"""

import asyncio
import os
import sys

from dotenv import load_dotenv

load_dotenv()

import mcp.types as types
from mcp import ClientSession
from mcp.client.streamable_http import streamablehttp_client
from mcp.server import Server
from mcp.server.stdio import stdio_server

import auth as _auth


def _build_headers() -> dict:
    """Build AEP auth headers for the active org profile."""
    cfg = _auth._active_cfg()
    token = _auth.get_access_token()
    api_key = cfg.get("api_key") or cfg.get("client_id") or os.environ.get("AEP_API_KEY", "")
    org_id = cfg.get("org_id") or os.environ.get("AEP_ORG_ID", "")
    return {
        "Authorization": f"Bearer {token}",
        "x-api-key": api_key,
        "x-gw-ims-org-id": org_id,
    }


async def run() -> None:
    url = os.getenv("RTCDP_MCP_URL", "https://rtcdp-mcp.adobe.io/mcp").strip()
    profile = _auth.get_active_profile() or "env"
    print(f"Connecting to RT-CDP MCP server: {url}  (profile={profile})", file=sys.stderr)

    headers = _build_headers()

    async with streamablehttp_client(url, headers=headers) as (read, write, _):
        async with ClientSession(read, write) as upstream:
            init_result = await upstream.initialize()
            server_name = getattr(init_result.serverInfo, "name", "rtcdp-upstream")
            server_version = getattr(init_result.serverInfo, "version", "?")
            print(f"Connected: {server_name} v{server_version}", file=sys.stderr)

            tools_result = await upstream.list_tools()
            available_tools: list[types.Tool] = tools_result.tools
            print(f"Proxying {len(available_tools)} tools", file=sys.stderr)

            proxy = Server("rtcdp-proxy")

            @proxy.list_tools()
            async def list_tools() -> list[types.Tool]:
                return available_tools

            @proxy.call_tool()
            async def call_tool(
                name: str,
                arguments: dict,
            ) -> list[types.TextContent | types.ImageContent | types.EmbeddedResource]:
                result = await upstream.call_tool(name, arguments or {})
                return result.content

            upstream_caps = init_result.capabilities
            if getattr(upstream_caps, "resources", None):

                @proxy.list_resources()
                async def list_resources() -> list[types.Resource]:
                    r = await upstream.list_resources()
                    return r.resources

                @proxy.read_resource()
                async def read_resource(
                    uri: types.AnyUrl,
                ) -> str | bytes:
                    r = await upstream.read_resource(uri)
                    if r.contents:
                        first = r.contents[0]
                        return getattr(first, "text", None) or getattr(first, "blob", b"")
                    return ""

            async with stdio_server() as (stdio_read, stdio_write):
                await proxy.run(
                    stdio_read,
                    stdio_write,
                    proxy.create_initialization_options(),
                )


if __name__ == "__main__":
    asyncio.run(run())
