"""
Adobe Journey Optimizer (AJO) tools — journeys, campaigns, offers, and offer decisioning.

API base: https://platform.adobe.io
  Journeys & Campaigns : /data/core/ajo/
  Offer Decisioning    : /data/core/dps/      (Decision Platform Service)

Verify exact paths against the AJO REST API reference at:
  https://developer.adobe.com/journey-optimizer/api-reference/
"""

from auth import aep_get, aep_post
from tools.usage_logger import track

_AJO = "/data/core/ajo"
_DPS = "/data/core/dps"


def register(mcp) -> None:

    # ── Journeys ─────────────────────────────────────────────────────────────

    @mcp.tool()
    @track("list_journeys")
    def list_journeys(
        sandbox: str = "",
        limit: int = 20,
        start: int = 0,
        status: str = "",
    ) -> dict:
        """List AJO journey definitions.

        Args:
            sandbox: Sandbox name.
            limit: Max records.
            start: Pagination offset.
            status: Filter by status (DRAFT, LIVE, FINISHED, CLOSED).
        """
        try:
            params: dict = {"limit": limit, "start": start}
            if status:
                params["status"] = status
            return aep_get(f"{_AJO}/journeys", sandbox=sandbox or None, params=params)
        except Exception as exc:
            return {"error": str(exc)}

    @mcp.tool()
    @track("get_journey")
    def get_journey(journey_id: str, sandbox: str = "") -> dict:
        """Get details for a specific AJO journey.

        Args:
            journey_id: Journey ID.
            sandbox: Sandbox name.
        """
        try:
            return aep_get(f"{_AJO}/journeys/{journey_id}", sandbox=sandbox or None)
        except Exception as exc:
            return {"error": str(exc)}

    @mcp.tool()
    @track("list_journey_versions")
    def list_journey_versions(journey_id: str, sandbox: str = "") -> dict:
        """List all published versions of a journey.

        Args:
            journey_id: Journey ID.
            sandbox: Sandbox name.
        """
        try:
            return aep_get(
                f"{_AJO}/journeys/{journey_id}/versions",
                sandbox=sandbox or None,
            )
        except Exception as exc:
            return {"error": str(exc)}

    # ── Campaigns ────────────────────────────────────────────────────────────

    @mcp.tool()
    @track("list_campaigns")
    def list_campaigns(
        sandbox: str = "",
        limit: int = 20,
        start: int = 0,
        status: str = "",
    ) -> dict:
        """List AJO campaigns.

        Args:
            sandbox: Sandbox name.
            limit: Max records.
            start: Pagination offset.
            status: Filter by status (DRAFT, LIVE, COMPLETED, STOPPED, etc.).
        """
        try:
            params: dict = {"limit": limit, "start": start}
            if status:
                params["status"] = status
            return aep_get(f"{_AJO}/campaigns", sandbox=sandbox or None, params=params)
        except Exception as exc:
            return {"error": str(exc)}

    @mcp.tool()
    @track("get_campaign")
    def get_campaign(campaign_id: str, sandbox: str = "") -> dict:
        """Get details for a specific AJO campaign.

        Args:
            campaign_id: Campaign ID.
            sandbox: Sandbox name.
        """
        try:
            return aep_get(f"{_AJO}/campaigns/{campaign_id}", sandbox=sandbox or None)
        except Exception as exc:
            return {"error": str(exc)}

    # ── Offer Library (Decision Management) ─────────────────────────────────

    @mcp.tool()
    @track("list_offers")
    def list_offers(
        sandbox: str = "",
        offer_type: str = "personalized",
        limit: int = 20,
        start: int = 0,
    ) -> dict:
        """List offers from the Offer Library.

        Args:
            sandbox: Sandbox name.
            offer_type: 'personalized' or 'fallback'.
            limit: Max records.
            start: Pagination offset.
        """
        try:
            return aep_get(
                f"{_DPS}/offers",
                sandbox=sandbox or None,
                params={"offer-type": offer_type, "limit": limit, "start": start},
            )
        except Exception as exc:
            return {"error": str(exc)}

    @mcp.tool()
    @track("get_offer")
    def get_offer(offer_id: str, sandbox: str = "") -> dict:
        """Get details for a specific personalized offer.

        Args:
            offer_id: Offer ID.
            sandbox: Sandbox name.
        """
        try:
            return aep_get(f"{_DPS}/offers/{offer_id}", sandbox=sandbox or None)
        except Exception as exc:
            return {"error": str(exc)}

    @mcp.tool()
    @track("list_placements")
    def list_placements(sandbox: str = "", limit: int = 20) -> dict:
        """List offer placements (channels/surfaces where offers appear).

        Args:
            sandbox: Sandbox name.
            limit: Max records.
        """
        try:
            return aep_get(
                f"{_DPS}/placements",
                sandbox=sandbox or None,
                params={"limit": limit},
            )
        except Exception as exc:
            return {"error": str(exc)}

    @mcp.tool()
    @track("list_collections")
    def list_collections(sandbox: str = "", limit: int = 20) -> dict:
        """List offer collections (curated groups of offers).

        Args:
            sandbox: Sandbox name.
            limit: Max records.
        """
        try:
            return aep_get(
                f"{_DPS}/offer-collections",
                sandbox=sandbox or None,
                params={"limit": limit},
            )
        except Exception as exc:
            return {"error": str(exc)}

    @mcp.tool()
    @track("list_offer_activities")
    def list_offer_activities(sandbox: str = "", limit: int = 20) -> dict:
        """List offer activities (decisions) — the logic that selects the best offer.

        Args:
            sandbox: Sandbox name.
            limit: Max records.
        """
        try:
            return aep_get(
                f"{_DPS}/offer-decisions",
                sandbox=sandbox or None,
                params={"limit": limit},
            )
        except Exception as exc:
            return {"error": str(exc)}

    @mcp.tool()
    @track("get_offer_activity")
    def get_offer_activity(activity_id: str, sandbox: str = "") -> dict:
        """Get details for a specific offer activity (decision).

        Args:
            activity_id: Offer activity ID.
            sandbox: Sandbox name.
        """
        try:
            return aep_get(f"{_DPS}/offer-decisions/{activity_id}", sandbox=sandbox or None)
        except Exception as exc:
            return {"error": str(exc)}

    @mcp.tool()
    @track("create_eligibility_rule")
    def create_eligibility_rule(
        name: str,
        pql: str,
        description: str = "",
        sandbox: str = "",
    ) -> dict:
        """Create an AJO offer eligibility rule (offer-rule) with a PQL expression.

        Args:
            name: Display name for the rule.
            pql: PQL expression string.
            description: Optional description.
            sandbox: Sandbox name.
        """
        try:
            body: dict = {
                "name": name,
                "condition": {
                    "type": "PQL",
                    "format": "pql/text",
                    "value": pql,
                },
            }
            if description:
                body["description"] = description
            return aep_post(f"{_DPS}/offer-rules", body, sandbox=sandbox or None)
        except Exception as exc:
            return {"error": str(exc)}

    @mcp.tool()
    @track("list_ranking_formulas")
    def list_ranking_formulas(sandbox: str = "", limit: int = 20) -> dict:
        """List offer ranking formulas used for AI-ranked offer decisioning.

        Args:
            sandbox: Sandbox name.
            limit: Max records.
        """
        try:
            return aep_get(
                f"{_DPS}/ranking-formulas",
                sandbox=sandbox or None,
                params={"limit": limit},
            )
        except Exception as exc:
            return {"error": str(exc)}
