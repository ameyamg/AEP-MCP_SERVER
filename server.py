"""
AEP MCP Server — FastMCP entrypoint.

All tool definitions live in tools/*.py; this file wires them together.

Run directly:
  python server.py

Or register in Claude Code (.claude/mcp_servers.json):
  {
    "aep": {
      "command": "python",
      "args": ["/path/to/aep-mcp-server/server.py"]
    }
  }
"""

from dotenv import load_dotenv

load_dotenv()

from mcp.server.fastmcp import FastMCP
from tools import (
    access_control,
    ajo,
    cja,
    computed_attributes,
    data_hygiene,
    data_prep,
    datasets,
    design,
    erd,
    flows,
    observability,
    orgs,
    profiles,
    query,
    schemas,
    segments,
)

mcp = FastMCP(
    "AEP MCP Server",
    instructions=(
        "Tools for Adobe Experience Platform (AEP) and Adobe Journey Optimizer (AJO). "
        "Covers datasets, XDM schemas, real-time profiles, identity namespaces, "
        "audience segments, SQL queries, AJO journeys, campaigns, offer decisioning, "
        "Flow Service (sources/destinations/dataflows), Observability Insights (metrics "
        "and alerts), Data Hygiene (dataset TTL and record deletes), Data Prep (mapping "
        "sets and expression validation), Computed Attributes, and Access Control "
        "(roles, permissions, and effective policies). "
        "CJA tools (cja_*) use Data View IDs instead of sandboxes. "
        "All AEP tools accept an optional `sandbox` parameter; if omitted they use the "
        "AEP_SANDBOX_NAME environment variable or the active org profile's sandbox."
    ),
)

# Register all tool domains
datasets.register(mcp)
design.register(mcp)
erd.register(mcp)
schemas.register(mcp)
profiles.register(mcp)
segments.register(mcp)
query.register(mcp)
ajo.register(mcp)
cja.register(mcp)
flows.register(mcp)
observability.register(mcp)
data_hygiene.register(mcp)
data_prep.register(mcp)
computed_attributes.register(mcp)
access_control.register(mcp)
orgs.register(mcp)

if __name__ == "__main__":
    import os
    transport = os.getenv("MCP_TRANSPORT", "stdio")
    if transport == "sse":
        port = int(os.getenv("PORT", "8080"))
        mcp.settings.host = "0.0.0.0"
        mcp.settings.port = port
        mcp.run(transport="sse")
    else:
        mcp.run(transport="stdio")
