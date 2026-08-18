#!/usr/bin/env bash
set -euo pipefail

REPO_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

echo "=== AEP MCP Server — Codespace setup ==="

# ── Python environment ────────────────────────────────────────────────────────

echo "Creating virtual environment..."
python3 -m venv "$REPO_DIR/.venv"
"$REPO_DIR/.venv/bin/pip" install --quiet --upgrade pip
"$REPO_DIR/.venv/bin/pip" install --quiet -r "$REPO_DIR/requirements.txt"
echo "Dependencies installed  ✓"

# ── Pre-commit hook ───────────────────────────────────────────────────────────

if [[ -f "$REPO_DIR/scripts/install_hooks.py" ]]; then
  "$REPO_DIR/.venv/bin/python" "$REPO_DIR/scripts/install_hooks.py" 2>/dev/null && echo "Pre-commit hook installed  ✓" || true
fi

# ── orgs.json from Codespace secret ──────────────────────────────────────────

if [[ -n "${ORGS_JSON:-}" ]]; then
  echo "$ORGS_JSON" > "$REPO_DIR/orgs.json"
  echo "orgs.json written from ORGS_JSON secret  ✓"
elif [[ ! -f "$REPO_DIR/orgs.json" ]]; then
  cp "$REPO_DIR/orgs.example.json" "$REPO_DIR/orgs.json"
  echo ""
  echo "⚠️  No ORGS_JSON secret found — orgs.example.json copied to orgs.json."
  echo "   Add your Adobe credentials to orgs.json, or set the ORGS_JSON"
  echo "   Codespace secret so future Codespaces are fully automatic."
fi

# ── .mcp.json for Claude Code ────────────────────────────────────────────────

cat > "$REPO_DIR/.mcp.json" <<EOF
{
  "mcpServers": {
    "aep": {
      "command": "$REPO_DIR/.venv/bin/python",
      "args": ["$REPO_DIR/server.py"]
    }
  }
}
EOF
echo ".mcp.json written  ✓"

# ── Claude Code CLI ──────────────────────────────────────────────────────────

if command -v npm &>/dev/null; then
  echo "Installing Claude Code CLI..."
  npm install -g @anthropic-ai/claude-code --silent && echo "Claude Code installed  ✓"
fi

# ── Summary ───────────────────────────────────────────────────────────────────

echo ""
echo "=== Setup complete ==="
echo ""
echo "To start the server (SSE mode for Codespace port forwarding):"
echo "  MCP_TRANSPORT=sse PORT=8080 .venv/bin/python server.py"
