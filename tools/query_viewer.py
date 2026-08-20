"""
tools/query_viewer.py — view_query_results MCP tool

Runs a SQL query via QS PostgreSQL, generates a self-contained HTML artifact
(table view + Raw JSON toggle, syntax-highlighted), writes to /tmp/, and
returns the file path for Claude to read and publish as an artifact.
"""

import html as _html
import json
import time

from tools.usage_logger import track

# ── CSS ──────────────────────────────────────────────────────────────────────
_CSS = """
<style>
:root {
  --bg:#F4F7FB; --surface:#FFFFFF; --surface2:#F0F4FA; --surface3:#E8EEF8;
  --border:#DDE4EF; --text:#0C2340; --text2:#4A5E78; --muted:#7A8FA8;
  --accent:#1473E6; --accent-bg:rgba(20,115,230,0.10);
  --mono:'SF Mono','Fira Code','Cascadia Code',monospace;
  --j-s:#0E7490; --j-n:#065F46; --j-k:#7C3AED;
  --topbar:#1473E6; --topbar-text:#fff;
}
@media (prefers-color-scheme:dark) {
  :root:not([data-theme="light"]) {
    --bg:#0D1626; --surface:#152035; --surface2:#1C2B42; --surface3:#243450;
    --border:#263A55; --text:#E2EAF4; --text2:#94AABF; --muted:#566E8A;
    --accent:#4A9EE5; --accent-bg:rgba(74,158,229,0.12);
    --j-s:#67E8F9; --j-n:#6EE7B7; --j-k:#C084FC;
    --topbar:#1C2B42; --topbar-text:#E2EAF4;
  }
}
:root[data-theme="dark"] {
  --bg:#0D1626; --surface:#152035; --surface2:#1C2B42; --surface3:#243450;
  --border:#263A55; --text:#E2EAF4; --text2:#94AABF; --muted:#566E8A;
  --accent:#4A9EE5; --accent-bg:rgba(74,158,229,0.12);
  --j-s:#67E8F9; --j-n:#6EE7B7; --j-k:#C084FC;
  --topbar:#1C2B42; --topbar-text:#E2EAF4;
}
*,*::before,*::after{box-sizing:border-box;margin:0;padding:0;}
body{background:var(--bg);color:var(--text);font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',system-ui,sans-serif;font-size:14px;line-height:1.5;}

.topbar{background:var(--topbar);color:var(--topbar-text);padding:10px 24px;display:flex;align-items:center;justify-content:space-between;}
.topbar-title{font-size:13px;font-weight:600;letter-spacing:.02em;}
.topbar-sub{font-size:11px;opacity:.75;margin-top:1px;}

header{background:var(--surface);border-bottom:1px solid var(--border);padding:12px 24px;position:sticky;top:0;z-index:20;}
.header-row{display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:10px;}
.chips{display:flex;flex-wrap:wrap;gap:6px;}
.chip{display:inline-flex;align-items:center;gap:5px;border:1px solid var(--border);border-radius:20px;padding:3px 10px;font-size:11.5px;color:var(--text2);background:var(--surface2);font-variant-numeric:tabular-nums;}
.chip strong{color:var(--text);font-weight:600;}
.chip-dot{width:7px;height:7px;border-radius:50%;flex-shrink:0;}
.toggle{display:flex;background:var(--surface2);border:1px solid var(--border);border-radius:8px;padding:3px;gap:2px;}
.toggle-btn{padding:5px 13px;border-radius:6px;border:none;background:transparent;color:var(--muted);font-size:12px;font-weight:500;cursor:pointer;transition:all 120ms;white-space:nowrap;}
.toggle-btn.active{background:var(--surface);color:var(--text);box-shadow:0 1px 3px rgba(0,0,0,.12);font-weight:600;}
.toggle-btn:hover:not(.active){color:var(--text);}

.sql-bar{background:var(--surface2);border-bottom:1px solid var(--border);padding:8px 24px;}
.sql-label{font-size:10.5px;font-weight:600;letter-spacing:.07em;text-transform:uppercase;color:var(--muted);margin-bottom:3px;}
.sql-text{font-family:var(--mono);font-size:12px;color:var(--text2);white-space:pre-wrap;word-break:break-all;max-height:56px;overflow:hidden;}
.sql-text.expanded{max-height:none;}
.sql-expand{font-size:11px;color:var(--accent);cursor:pointer;background:none;border:none;padding:2px 0 0;display:block;}

main{padding:20px 24px;}
.table-wrap{background:var(--surface);border:1px solid var(--border);border-radius:10px;overflow:hidden;overflow-x:auto;}
table{width:100%;border-collapse:collapse;min-width:400px;}
thead tr{background:var(--surface2);}
thead th{padding:9px 14px;text-align:left;font-size:11px;font-weight:600;letter-spacing:.07em;text-transform:uppercase;color:var(--muted);border-bottom:1px solid var(--border);white-space:nowrap;}
thead th:first-child{padding-left:18px;}thead th:last-child{padding-right:18px;}
tbody tr{border-bottom:1px solid var(--border);transition:background 100ms;}
tbody tr:last-child{border-bottom:none;}
tbody tr:hover{background:var(--surface2);}
td{padding:10px 14px;vertical-align:top;font-size:13px;}
td:first-child{padding-left:18px;}td:last-child{padding-right:18px;}
.footer{text-align:center;padding:9px;font-size:11.5px;color:var(--muted);background:var(--surface2);border-top:1px solid var(--border);}

.null-val{color:var(--muted);}
.mono-val{font-family:var(--mono);font-size:12px;}
.nested-toggle{cursor:pointer;font-family:var(--mono);font-size:12px;color:var(--accent);background:var(--accent-bg);padding:1px 7px;border-radius:4px;border:none;}
.nested-json{font-family:var(--mono);font-size:11.5px;background:var(--surface2);border:1px solid var(--border);border-radius:6px;padding:10px;margin-top:5px;white-space:pre;overflow-x:auto;max-width:640px;}
.j-s{color:var(--j-s);} .j-n{color:var(--j-n);} .j-k{color:var(--j-k);}

#view-raw{display:none;}
.raw-wrap{background:var(--surface);border:1px solid var(--border);border-radius:10px;overflow:hidden;}
.raw-toolbar{display:flex;justify-content:flex-end;padding:8px 14px;border-bottom:1px solid var(--border);background:var(--surface2);}
.copy-btn{font-size:11.5px;padding:4px 12px;border-radius:6px;border:1px solid var(--border);background:var(--surface);color:var(--text2);cursor:pointer;}
.copy-btn:hover{color:var(--text);}
.raw-pre{font-family:var(--mono);font-size:12px;padding:16px 20px;white-space:pre;overflow-x:auto;line-height:1.6;}
.empty-state{text-align:center;padding:48px 24px;color:var(--muted);font-size:13px;}
</style>
"""

# ── JS ────────────────────────────────────────────────────────────────────────
_JS = r"""
<script>
function switchView(v, btn) {
  document.getElementById('view-formatted').style.display = v === 'formatted' ? '' : 'none';
  document.getElementById('view-raw').style.display = v === 'raw' ? '' : 'none';
  document.querySelectorAll('.toggle-btn').forEach(function(b) { b.classList.remove('active'); });
  btn.classList.add('active');
}
function toggleNested(id) {
  var el = document.getElementById(id);
  if (!el) return;
  var open = el.style.display !== 'none';
  el.style.display = open ? 'none' : '';
  if (!open && !el.dataset.hl) {
    el.innerHTML = highlight(el.textContent);
    el.dataset.hl = '1';
  }
}
function expandSql() {
  var el = document.getElementById('sql-text');
  var btn = document.getElementById('sql-expand-btn');
  el.classList.toggle('expanded');
  btn.textContent = el.classList.contains('expanded') ? 'show less ▴' : 'show more ▾';
}
function copyRaw() {
  var pre = document.getElementById('raw-pre');
  navigator.clipboard.writeText(pre ? pre.dataset.raw || pre.textContent : '').catch(function(){});
}
function highlight(text) {
  var t = text.replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;');
  t = t.replace(/"((?:[^"\\\\]|\\\\.)*)"(\s*):/g, '<span class="j-k">"$1"</span>$2:');
  t = t.replace(/:\s*"((?:[^"\\\\]|\\\\.)*)"(?=[,\n\r\]\}]|$)/g, ': <span class="j-s">"$1"</span>');
  t = t.replace(/:\s*(-?\d+(?:\.\d+)?(?:[eE][+-]?\d+)?)(?=[,\n\r\]\}]|$)/g, ': <span class="j-n">$1</span>');
  t = t.replace(/:\s*(true|false|null)(?=[,\n\r\]\}]|$)/g, ': <span class="j-k">$1</span>');
  return t;
}
document.addEventListener('DOMContentLoaded', function() {
  var rawPre = document.getElementById('raw-pre');
  if (rawPre) {
    rawPre.dataset.raw = rawPre.textContent;
    rawPre.innerHTML = highlight(rawPre.textContent);
  }
  var sqlEl = document.getElementById('sql-text');
  var sqlBtn = document.getElementById('sql-expand-btn');
  if (sqlEl && sqlBtn && sqlEl.scrollHeight <= sqlEl.clientHeight + 4) {
    sqlBtn.style.display = 'none';
  }
  document.querySelectorAll('.nested-json[data-hl="0"]').forEach(function(el) {
    // highlight on first expand, not on load (perf)
  });
});
</script>
"""

# ── cell renderer ─────────────────────────────────────────────────────────────
_nested_counter = 0


def _sanitize(val):
    """Convert psycopg2 non-JSON-serializable types to plain Python types."""
    import datetime, decimal
    if val is None:
        return None
    if isinstance(val, (bool, int, float, str)):
        return val
    if isinstance(val, (datetime.date, datetime.datetime, datetime.time)):
        return val.isoformat()
    if isinstance(val, decimal.Decimal):
        return float(val)
    if isinstance(val, (list, tuple)):
        return [_sanitize(v) for v in val]
    if isinstance(val, dict):
        return {k: _sanitize(v) for k, v in val.items()}
    return str(val)


def _cell_html(val, col_idx: int, row_idx: int) -> str:
    if val is None:
        return '<span class="null-val">—</span>'

    # dict / list → collapsible JSON block
    if isinstance(val, (dict, list)):
        return _nested_block(val, col_idx, row_idx)

    s = str(val)

    # string that is JSON → expand
    if s.strip().startswith(("{", "[")):
        try:
            parsed = json.loads(s)
            return _nested_block(parsed, col_idx, row_idx)
        except Exception:
            pass

    # long string → truncate with title tooltip
    if len(s) > 140:
        esc = _html.escape(s)
        return f'<span class="mono-val" title="{esc}">{_html.escape(s[:140])}…</span>'

    return _html.escape(s)


def _nested_block(val, col_idx: int, row_idx: int) -> str:
    uid = f"n{col_idx}r{row_idx}"
    pretty = json.dumps(val, indent=2, ensure_ascii=False)
    esc = _html.escape(pretty)
    preview = "{…}" if isinstance(val, dict) else "[…]"
    return (
        f'<button class="nested-toggle" onclick="toggleNested(\'{uid}\')">{preview}</button>'
        f'<pre class="nested-json" id="{uid}" style="display:none" data-hl="0">{esc}</pre>'
    )


# ── HTML builder ──────────────────────────────────────────────────────────────
def _generate_html(sql: str, columns: list, rows: list, sandbox: str, title: str) -> str:
    row_count = len(rows)
    col_count = len(columns)
    ts = time.strftime("%Y-%m-%d %H:%M UTC", time.gmtime())

    chips = (
        f'<span class="chip"><span class="chip-dot" style="background:#1473E6"></span>'
        f'<strong>{row_count}</strong> row{"s" if row_count != 1 else ""}</span>'
        f'<span class="chip"><strong>{col_count}</strong> col{"s" if col_count != 1 else ""}</span>'
        f'<span class="chip">{_html.escape(sandbox)}</span>'
        f'<span class="chip">{_html.escape(ts)}</span>'
    )

    th_html = "".join(f"<th>{_html.escape(c)}</th>" for c in columns)

    tbody_parts = []
    for r_idx, row in enumerate(rows):
        cells = "".join(
            f"<td>{_cell_html(row.get(c), c_idx, r_idx)}</td>"
            for c_idx, c in enumerate(columns)
        )
        tbody_parts.append(f"<tr>{cells}</tr>")
    tbody_html = "\n".join(tbody_parts)

    raw_json = json.dumps(rows, indent=2, ensure_ascii=False)
    raw_esc = _html.escape(raw_json)
    sql_esc = _html.escape(sql.strip())
    title_esc = _html.escape(title)
    sandbox_esc = _html.escape(sandbox)
    footer = f"{row_count} row{'s' if row_count != 1 else ''} returned"

    empty = (
        '<div class="empty-state">No rows returned.</div>'
        if row_count == 0
        else f'<table><thead><tr>{th_html}</tr></thead><tbody>{tbody_html}</tbody></table>'
             f'<div class="footer">{footer}</div>'
    )

    return "\n".join([
        "<!DOCTYPE html>",
        '<html lang="en">',
        "<head>",
        '<meta charset="UTF-8">',
        '<meta name="viewport" content="width=device-width, initial-scale=1">',
        f"<title>{title_esc}</title>",
        _CSS,
        "</head>",
        "<body>",
        f'<div class="topbar">',
        f'  <div><div class="topbar-title">{title_esc}</div>',
        f'  <div class="topbar-sub">AEP Query Service · {sandbox_esc}</div></div>',
        "</div>",
        "<header>",
        f'  <div class="header-row">',
        f'    <div class="chips">{chips}</div>',
        '    <div class="toggle">',
        '      <button class="toggle-btn active" onclick="switchView(\'formatted\', this)">Formatted</button>',
        '      <button class="toggle-btn" onclick="switchView(\'raw\', this)">Raw JSON</button>',
        "    </div>",
        "  </div>",
        "</header>",
        '<div class="sql-bar">',
        '  <div class="sql-label">SQL</div>',
        f'  <div class="sql-text" id="sql-text">{sql_esc}</div>',
        '  <button class="sql-expand" id="sql-expand-btn" onclick="expandSql()">show more ▾</button>',
        "</div>",
        "<main>",
        '  <div id="view-formatted">',
        '    <div class="table-wrap">',
        f"      {empty}",
        "    </div>",
        "  </div>",
        '  <div id="view-raw">',
        '    <div class="raw-wrap">',
        '      <div class="raw-toolbar">',
        '        <button class="copy-btn" onclick="copyRaw()">Copy JSON</button>',
        "      </div>",
        f'      <pre class="raw-pre" id="raw-pre">{raw_esc}</pre>',
        "    </div>",
        "  </div>",
        "</main>",
        _JS,
        "</body>",
        "</html>",
    ])


# ── text summary ──────────────────────────────────────────────────────────────
def _text_summary(sql: str, columns: list, rows: list, sandbox: str, title: str) -> str:
    lines = [f"**{title}** — {len(rows)} row{'s' if len(rows) != 1 else ''} in `{sandbox}`"]
    if not rows:
        lines.append("_No rows returned._")
        return "\n".join(lines)

    lines.append(f"Columns: {', '.join(f'`{c}`' for c in columns)}")
    lines.append("")

    # preview up to 5 rows
    preview_rows = rows[:5]
    # header
    header = " | ".join(columns)
    sep = " | ".join("---" for _ in columns)
    lines.append(f"| {header} |")
    lines.append(f"| {sep} |")
    for row in preview_rows:
        cells = []
        for c in columns:
            v = row.get(c)
            if v is None:
                cells.append("—")
            elif isinstance(v, (dict, list)):
                cells.append("{…}")
            else:
                s = str(v).replace("|", "\\|").replace("\n", " ")
                cells.append(s[:60] + ("…" if len(s) > 60 else ""))
        lines.append(f"| {' | '.join(cells)} |")

    if len(rows) > 5:
        lines.append(f"_… and {len(rows) - 5} more row{'s' if len(rows) - 5 != 1 else ''}_")

    return "\n".join(lines)


# ── register ───────────────────────────────────────────────────────────────────
def register(mcp):
    @mcp.tool()
    @track("view_query_results")
    def view_query_results(
        sql: str,
        sandbox: str = "",
        row_limit: int = 500,
        title: str = "",
    ) -> dict:
        """Run a SQL query and return a formatted HTML artifact with the results.

        Executes the query via QS PostgreSQL (same as run_query_sync), then
        generates a self-contained HTML page with a Formatted table view and
        Raw JSON toggle. Writes the page to /tmp/ and returns the file path
        for Claude to read and publish as an artifact.

        Args:
            sql: SQL SELECT statement to execute.
            sandbox: Sandbox name (defaults to active profile sandbox).
            row_limit: Max rows to return (default 500, max 5000).
            title: Optional display title for the artifact (auto-generated from SQL if omitted).
        """
        try:
            import psycopg2
            from auth import aep_get, get_active_sandbox

            effective_sandbox = sandbox or get_active_sandbox()

            cp = aep_get(
                "/data/foundation/query/connection_parameters",
                sandbox=effective_sandbox,
            )

            conn = psycopg2.connect(
                host=cp["host"],
                port=cp["port"],
                dbname=cp["dbName"],
                user=cp["username"],
                password=cp["token"],
                sslmode="require",
                connect_timeout=30,
            )
            try:
                cur = conn.cursor()
                cur.execute(sql)
                cols = [d[0] for d in cur.description] if cur.description else []
                limit = min(max(1, row_limit), 5000)
                raw_rows = cur.fetchmany(limit)
                rows = [
                    {c: _sanitize(v) for c, v in zip(cols, row)}
                    for row in raw_rows
                ]
                cur.close()
            finally:
                conn.close()

            # derive title from SQL if not provided
            if not title:
                first_line = sql.strip().splitlines()[0][:80]
                title = first_line if len(first_line) > 5 else "Query Results"

            html_out = _generate_html(sql, cols, rows, effective_sandbox, title)

            slug = title[:40].replace(" ", "-").replace("/", "-").lower()
            ts_slug = time.strftime("%Y%m%d-%H%M%S", time.gmtime())
            html_path = f"/tmp/aep-query-{slug}-{ts_slug}.html"
            with open(html_path, "w", encoding="utf-8") as fh:
                fh.write(html_out)

            text = _text_summary(sql, cols, rows, effective_sandbox, title)

            return {
                "text_summary": text,
                "html_file": html_path,
                "row_count": len(rows),
                "columns": cols,
                "instruction": (
                    f"Display the text_summary in your response. "
                    f"Then read {html_path} and publish it as an artifact "
                    f"titled '{title}'."
                ),
            }
        except Exception as exc:
            return {"error": str(exc)}
