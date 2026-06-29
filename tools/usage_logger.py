"""
CSV usage-tracking decorator.

Logs every tool invocation with timing, org context, response size,
and an estimated token count for the tool result returned to Claude.

Token estimation:
  Each tool returns a JSON payload that becomes a tool-result message in
  Claude's context. We estimate tokens as ceil(response_bytes / 4), which
  matches Anthropic's rough 1 token ≈ 4 bytes rule for JSON/English text.
  This is the dominant per-call token cost — input params are tiny by
  comparison.

CSV columns:
  timestamp, profile, sandbox, tool, params,
  duration_ms, success, error, response_bytes, estimated_tokens
"""

import csv
import inspect
import json
import math
import os
from datetime import datetime, timezone
from functools import wraps
from typing import Any, Callable, Optional

LOG_FILE = os.getenv("AEP_USAGE_LOG", "aep_usage.csv")

_FIELDNAMES = [
    "timestamp",
    "profile",
    "sandbox",
    "tool",
    "params",
    "duration_ms",
    "success",
    "error",
    "response_bytes",
    "estimated_tokens",
]

_header_written = False


def _ensure_header() -> None:
    global _header_written
    if _header_written:
        return
    if not os.path.exists(LOG_FILE):
        with open(LOG_FILE, "w", newline="") as f:
            csv.DictWriter(f, fieldnames=_FIELDNAMES).writeheader()
    else:
        # Check if existing file has old schema (missing new columns); if so, back it up.
        with open(LOG_FILE, "r", newline="") as f:
            existing = csv.DictReader(f).fieldnames or []
        if set(existing) != set(_FIELDNAMES):
            backup = LOG_FILE.replace(".csv", "_backup.csv")
            os.rename(LOG_FILE, backup)
            with open(LOG_FILE, "w", newline="") as f:
                csv.DictWriter(f, fieldnames=_FIELDNAMES).writeheader()
    _header_written = True


def _get_context() -> tuple[str, str]:
    """Return (active_profile, active_sandbox) without hard-failing if auth is unavailable."""
    try:
        import auth
        return auth.get_active_profile() or "env", auth.get_active_sandbox() or "default"
    except Exception:
        return "unknown", "unknown"


def _estimate_tokens(result: Any) -> tuple[int, int]:
    """Return (response_bytes, estimated_tokens) for a tool result."""
    try:
        payload = json.dumps(result, default=str)
        size = len(payload.encode("utf-8"))
        tokens = math.ceil(size / 4)
        return size, tokens
    except Exception:
        return 0, 0


def _write_row(
    tool: str,
    params: dict,
    start: datetime,
    error: Optional[str],
    result: Any = None,
) -> None:
    _ensure_header()
    duration = (datetime.now(timezone.utc) - start).total_seconds() * 1000
    safe_params = {k: v for k, v in params.items() if "token" not in k.lower() and "secret" not in k.lower()}
    profile, sandbox = _get_context()
    response_bytes, estimated_tokens = _estimate_tokens(result)

    with open(LOG_FILE, "a", newline="") as f:
        csv.DictWriter(f, fieldnames=_FIELDNAMES).writerow(
            {
                "timestamp": start.isoformat(),
                "profile": profile,
                "sandbox": sandbox,
                "tool": tool,
                "params": str(safe_params),
                "duration_ms": round(duration, 2),
                "success": error is None,
                "error": error or "",
                "response_bytes": response_bytes,
                "estimated_tokens": estimated_tokens,
            }
        )


def track(tool_name: str) -> Callable:
    """Decorator that logs tool invocations with token estimates to AEP_USAGE_LOG."""

    def decorator(func: Callable) -> Callable:
        if inspect.iscoroutinefunction(func):

            @wraps(func)
            async def async_wrapper(*args: Any, **kwargs: Any) -> Any:
                start = datetime.now(timezone.utc)
                err: Optional[str] = None
                result: Any = None
                try:
                    result = await func(*args, **kwargs)
                    return result
                except Exception as exc:
                    err = str(exc)
                    raise
                finally:
                    _write_row(tool_name, kwargs, start, err, result)

            return async_wrapper

        @wraps(func)
        def sync_wrapper(*args: Any, **kwargs: Any) -> Any:
            start = datetime.now(timezone.utc)
            err: Optional[str] = None
            result: Any = None
            try:
                result = func(*args, **kwargs)
                return result
            except Exception as exc:
                err = str(exc)
                raise
            finally:
                _write_row(tool_name, kwargs, start, err, result)

        return sync_wrapper

    return decorator
