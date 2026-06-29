"""Observability Insights — platform metrics and alert subscriptions."""

from auth import aep_get, aep_post
from tools.usage_logger import track

_OBS = "/data/infrastructure/observability/insights"


def register(mcp) -> None:

    # ── Metrics ──────────────────────────────────────────────────────────────

    @mcp.tool()
    @track("get_metrics")
    def get_metrics(
        metrics: list,
        start_time: str,
        end_time: str,
        granularity: str = "DAILY",
        filters: list = None,
        sandbox: str = "",
    ) -> dict:
        """Retrieve observability metrics for AEP resources.

        Common metric IDs:
          - timeseries.ingestion.dataset.recordsuccess.count
          - timeseries.ingestion.dataset.size
          - timeseries.identity.dataset.recordsuccess.count
          - timeseries.profiles.dataset.recordsuccess.count

        Args:
            metrics: List of metric ID strings to retrieve.
            start_time: ISO-8601 start timestamp (e.g. '2024-01-01T00:00:00Z').
            end_time: ISO-8601 end timestamp.
            granularity: Time bucket — DAILY or PT1H (hourly).
            filters: Optional list of filter dicts, e.g.
                     [{"name": "dataSetId", "value": ["abc123"], "groupBy": true}].
            sandbox: Sandbox name.
        """
        try:
            body: dict = {
                "start": start_time,
                "end": end_time,
                "granularity": granularity,
                "metrics": [{"name": m} for m in metrics],
            }
            if filters:
                body["filters"] = filters
            return aep_post(f"{_OBS}/metrics", body, sandbox=sandbox or None)
        except Exception as exc:
            return {"error": str(exc)}

    # ── Alert Subscriptions ──────────────────────────────────────────────────

    @mcp.tool()
    @track("list_alert_subscriptions")
    def list_alert_subscriptions(sandbox: str = "", limit: int = 20) -> dict:
        """List all alert subscriptions in the org.

        Args:
            sandbox: Sandbox name.
            limit: Max records.
        """
        try:
            return aep_get(
                f"{_OBS}/alert-subscriptions",
                sandbox=sandbox or None,
                params={"limit": limit},
            )
        except Exception as exc:
            return {"error": str(exc)}

    @mcp.tool()
    @track("get_alert_subscription")
    def get_alert_subscription(subscription_id: str, sandbox: str = "") -> dict:
        """Get details for a specific alert subscription.

        Args:
            subscription_id: Alert subscription ID.
            sandbox: Sandbox name.
        """
        try:
            return aep_get(
                f"{_OBS}/alert-subscriptions/{subscription_id}",
                sandbox=sandbox or None,
            )
        except Exception as exc:
            return {"error": str(exc)}

    @mcp.tool()
    @track("get_alerts_by_feature")
    def get_alerts_by_feature(
        feature: str,
        sandbox: str = "",
        limit: int = 20,
    ) -> dict:
        """List alert subscriptions for a specific AEP feature.

        Args:
            feature: AEP feature name (e.g. 'sources', 'destinations', 'flows',
                     'datasets', 'ingestion', 'identity', 'profile', 'segments').
            sandbox: Sandbox name.
            limit: Max records.
        """
        try:
            return aep_get(
                f"{_OBS}/alert-subscriptions/objects/{feature}",
                sandbox=sandbox or None,
                params={"limit": limit},
            )
        except Exception as exc:
            return {"error": str(exc)}

    @mcp.tool()
    @track("subscribe_alert")
    def subscribe_alert(
        alert_id: str,
        notification_type: str = "EMAIL",
        sandbox: str = "",
    ) -> dict:
        """Subscribe to an alert by its alert ID.

        Args:
            alert_id: Alert type identifier
                      (e.g. 'sources_flow_run_failed', 'destination_flow_run_failed').
            notification_type: 'EMAIL' or 'IN_APP'.
            sandbox: Sandbox name.
        """
        try:
            body = {"alertId": alert_id, "notificationType": notification_type}
            return aep_post(
                f"{_OBS}/alert-subscriptions",
                body,
                sandbox=sandbox or None,
            )
        except Exception as exc:
            return {"error": str(exc)}

    # ── Alert Notifications (history) ────────────────────────────────────────

    @mcp.tool()
    @track("list_alert_notifications")
    def list_alert_notifications(
        sandbox: str = "",
        limit: int = 20,
        status: str = "",
    ) -> dict:
        """List historical alert notification events.

        Args:
            sandbox: Sandbox name.
            limit: Max records.
            status: Filter by status (TRIGGERED, RESOLVED).
        """
        try:
            params: dict = {"limit": limit}
            if status:
                params["status"] = status
            return aep_get(
                f"{_OBS}/alert-notifications",
                sandbox=sandbox or None,
                params=params,
            )
        except Exception as exc:
            return {"error": str(exc)}
