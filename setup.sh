#!/usr/bin/env bash
set -euo pipefail

REPO_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
VENV="$REPO_DIR/.venv"

echo "=== AEP MCP Server — setup ==="
echo ""

# ── Python check ─────────────────────────────────────────────────────────────

if ! command -v python3 &>/dev/null; then
  echo "ERROR: python3 not found. Install Python 3.10+ and re-run this script."
  exit 1
fi

PY_VERSION=$(python3 -c "import sys; print(f'{sys.version_info.major}.{sys.version_info.minor}')")
PY_MAJOR=$(python3 -c "import sys; print(sys.version_info.major)")
PY_MINOR=$(python3 -c "import sys; print(sys.version_info.minor)")

if [[ "$PY_MAJOR" -lt 3 || ("$PY_MAJOR" -eq 3 && "$PY_MINOR" -lt 10) ]]; then
  echo "ERROR: Python 3.10+ required (found $PY_VERSION)."
  exit 1
fi

echo "Python $PY_VERSION  ✓"

# ── Virtual environment ───────────────────────────────────────────────────────

if [[ -d "$VENV" ]]; then
  echo "Venv already exists — skipping creation."
else
  echo "Creating virtual environment..."
  python3 -m venv "$VENV"
fi

# ── Dependencies ─────────────────────────────────────────────────────────────

echo "Installing dependencies..."
"$VENV/bin/pip" install --quiet --upgrade pip
"$VENV/bin/pip" install --quiet -r "$REPO_DIR/requirements.txt"
echo "Dependencies installed  ✓"

# ── Pre-commit hook ───────────────────────────────────────────────────────────

if [[ -f "$REPO_DIR/scripts/install_hooks.py" ]]; then
  "$VENV/bin/python" "$REPO_DIR/scripts/install_hooks.py" 2>/dev/null && echo "Pre-commit hook installed  ✓" || true
fi

# ── Credentials check ────────────────────────────────────────────────────────

if [[ ! -f "$REPO_DIR/orgs.json" ]]; then
  echo ""
  echo "No orgs.json found — copying template..."
  cp "$REPO_DIR/orgs.example.json" "$REPO_DIR/orgs.json"
  echo "Edit orgs.json with your Adobe credentials before starting the server."
fi

# ── Summary ───────────────────────────────────────────────────────────────────

PYTHON_PATH="$VENV/bin/python"

echo ""
echo "=== Setup complete ==="
echo ""
echo "Venv Python path (use this in your MCP config):"
echo "  $PYTHON_PATH"
echo ""
echo "Add to .claude/mcp_servers.json:"
echo "  {"
echo "    \"aep\": {"
echo "      \"command\": \"$PYTHON_PATH\","
echo "      \"args\": [\"$REPO_DIR/server.py\"]"
echo "    }"
echo "  }"
echo ""
echo "Then restart Claude Code and run /mcp to connect."
