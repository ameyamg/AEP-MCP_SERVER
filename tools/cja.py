"""
Customer Journey Analytics (CJA) tools.

API base: https://cja.adobe.io
Auth: same IMS OAuth S2S token + org header as AEP — no x-sandbox-name header.
CJA scopes data via Data View ID (dataviewId) passed as a query parameter.

Covers:
  - Data Views & Connections (read)
  - Dimensions & Metrics catalog (read)
  - Calculated Metrics (CRUD)
  - Filters / Segments (CRUD)
  - Projects / Workspace panels (CRUD)
  - Annotations (CRUD)
  - Reports / analytics queries (run)
"""

from auth import cja_get, cja_post, cja_put, cja_delete
from tools.usage_logger import track


def register(mcp) -> None:

    # ── Data Views ────────────────────────────────────────────────────────────

    @mcp.tool()
    @track("cja_list_data_views")
    def cja_list_data_views(limit: int = 20, expansion: str = "") -> dict:
        """List all CJA data views accessible to the active org.

        Args:
            limit: Max records to return.
            expansion: Comma-separated fields to expand (e.g. 'settings,tags').
        """
        try:
            params: dict = {"limit": limit}
            if expansion:
                params["expansion"] = expansion
            return cja_get("/data/dataviews", params=params)
        except Exception as exc:
            return {"error": str(exc)}

    @mcp.tool()
    @track("cja_get_data_view")
    def cja_get_data_view(data_view_id: str, expansion: str = "") -> dict:
        """Get full details for a specific CJA data view.

        Args:
            data_view_id: Data view ID (e.g. dv_abc123).
            expansion: Comma-separated fields to expand.
        """
        try:
            params = {"expansion": expansion} if expansion else {}
            return cja_get(f"/data/dataviews/{data_view_id}", params=params)
        except Exception as exc:
            return {"error": str(exc)}

    # ── Connections ───────────────────────────────────────────────────────────

    @mcp.tool()
    @track("cja_list_connections")
    def cja_list_connections(limit: int = 20, expansion: str = "") -> dict:
        """List CJA connections (AEP dataset → CJA mappings).

        Args:
            limit: Max records to return.
            expansion: Comma-separated fields to expand.
        """
        try:
            params: dict = {"limit": limit}
            if expansion:
                params["expansion"] = expansion
            return cja_get("/data/connections", params=params)
        except Exception as exc:
            return {"error": str(exc)}

    @mcp.tool()
    @track("cja_get_connection")
    def cja_get_connection(connection_id: str) -> dict:
        """Get details for a specific CJA connection.

        Args:
            connection_id: Connection ID.
        """
        try:
            return cja_get(f"/data/connections/{connection_id}")
        except Exception as exc:
            return {"error": str(exc)}

    # ── Dimensions & Metrics catalog ─────────────────────────────────────────

    @mcp.tool()
    @track("cja_list_dimensions")
    def cja_list_dimensions(
        data_view_id: str,
        locale: str = "en_US",
        search: str = "",
        limit: int = 100,
    ) -> dict:
        """List all dimensions available in a CJA data view.

        Args:
            data_view_id: Data view ID to scope the lookup.
            locale: Locale for dimension labels (default en_US).
            search: Optional keyword filter on dimension name.
            limit: Max records.
        """
        try:
            params: dict = {"locale": locale, "limit": limit}
            if search:
                params["search"] = search
            return cja_get(f"/data/dataviews/{data_view_id}/dimensions", params=params)
        except Exception as exc:
            return {"error": str(exc)}

    @mcp.tool()
    @track("cja_list_metrics")
    def cja_list_metrics(
        data_view_id: str,
        locale: str = "en_US",
        search: str = "",
        limit: int = 100,
    ) -> dict:
        """List all metrics available in a CJA data view.

        Args:
            data_view_id: Data view ID to scope the lookup.
            locale: Locale for metric labels (default en_US).
            search: Optional keyword filter on metric name.
            limit: Max records.
        """
        try:
            params: dict = {"locale": locale, "limit": limit}
            if search:
                params["search"] = search
            return cja_get(f"/data/dataviews/{data_view_id}/metrics", params=params)
        except Exception as exc:
            return {"error": str(exc)}

    # ── Calculated Metrics ────────────────────────────────────────────────────

    @mcp.tool()
    @track("cja_list_calculated_metrics")
    def cja_list_calculated_metrics(
        limit: int = 20,
        filter_by_ids: str = "",
        expansion: str = "",
    ) -> dict:
        """List CJA calculated metrics.

        Args:
            limit: Max records.
            filter_by_ids: Comma-separated calculated metric IDs to filter.
            expansion: Comma-separated fields to expand (e.g. 'definition,tags').
        """
        try:
            params: dict = {"limit": limit}
            if filter_by_ids:
                params["filterByIds"] = filter_by_ids
            if expansion:
                params["expansion"] = expansion
            return cja_get("/calculatedmetrics", params=params)
        except Exception as exc:
            return {"error": str(exc)}

    @mcp.tool()
    @track("cja_get_calculated_metric")
    def cja_get_calculated_metric(metric_id: str, expansion: str = "") -> dict:
        """Get a specific CJA calculated metric by ID.

        Args:
            metric_id: Calculated metric ID.
            expansion: Comma-separated fields to expand.
        """
        try:
            params = {"expansion": expansion} if expansion else {}
            return cja_get(f"/calculatedmetrics/{metric_id}", params=params)
        except Exception as exc:
            return {"error": str(exc)}

    @mcp.tool()
    @track("cja_create_calculated_metric")
    def cja_create_calculated_metric(
        name: str,
        description: str,
        data_view_id: str,
        definition: dict,
        polarity: str = "positive",
        precision: int = 2,
        format: str = "DECIMAL",
    ) -> dict:
        """Create a new CJA calculated metric.

        Args:
            name: Display name.
            description: Human-readable description.
            data_view_id: Data view this metric belongs to.
            definition: Metric formula as a CJA definition object.
                Example for (Orders / Visits):
                {
                  "func": "calc-metric",
                  "version": [1, 0, 0],
                  "col": {
                    "func": "divide",
                    "col1": {"func": "metric", "name": "metrics/orders"},
                    "col2": {"func": "metric", "name": "metrics/visits"}
                  }
                }
            polarity: 'positive' (higher is better) or 'negative'.
            precision: Decimal places (0-10).
            format: 'DECIMAL', 'PERCENT', 'CURRENCY', 'TIME'.
        """
        try:
            body = {
                "name": name,
                "description": description,
                "rsid": data_view_id,
                "definition": definition,
                "polarity": polarity,
                "precision": precision,
                "type": format,
            }
            return cja_post("/calculatedmetrics", body)
        except Exception as exc:
            return {"error": str(exc)}

    @mcp.tool()
    @track("cja_update_calculated_metric")
    def cja_update_calculated_metric(metric_id: str, updates: dict) -> dict:
        """Update an existing CJA calculated metric (full replace).

        Args:
            metric_id: Calculated metric ID to update.
            updates: Full metric definition object (same shape as create).
        """
        try:
            return cja_put(f"/calculatedmetrics/{metric_id}", updates)
        except Exception as exc:
            return {"error": str(exc)}

    @mcp.tool()
    @track("cja_delete_calculated_metric")
    def cja_delete_calculated_metric(metric_id: str) -> dict:
        """Delete a CJA calculated metric.

        Args:
            metric_id: Calculated metric ID to delete.
        """
        try:
            result = cja_delete(f"/calculatedmetrics/{metric_id}")
            return result or {"status": "deleted", "id": metric_id}
        except Exception as exc:
            return {"error": str(exc)}

    # ── Filters (CJA Segments) ────────────────────────────────────────────────

    @mcp.tool()
    @track("cja_list_filters")
    def cja_list_filters(
        limit: int = 20,
        data_view_id: str = "",
        expansion: str = "",
    ) -> dict:
        """List CJA filters (equivalent to segments in AEP/AA).

        Args:
            limit: Max records.
            data_view_id: Scope to a specific data view.
            expansion: Comma-separated fields to expand (e.g. 'definition,tags').
        """
        try:
            params: dict = {"limit": limit}
            if data_view_id:
                params["rsids"] = data_view_id
            if expansion:
                params["expansion"] = expansion
            return cja_get("/segments", params=params)
        except Exception as exc:
            return {"error": str(exc)}

    @mcp.tool()
    @track("cja_get_filter")
    def cja_get_filter(filter_id: str, expansion: str = "") -> dict:
        """Get a specific CJA filter by ID.

        Args:
            filter_id: Filter ID.
            expansion: Comma-separated fields to expand.
        """
        try:
            params = {"expansion": expansion} if expansion else {}
            return cja_get(f"/segments/{filter_id}", params=params)
        except Exception as exc:
            return {"error": str(exc)}

    @mcp.tool()
    @track("cja_create_filter")
    def cja_create_filter(
        name: str,
        description: str,
        data_view_id: str,
        definition: dict,
    ) -> dict:
        """Create a CJA filter (segment).

        Args:
            name: Display name.
            description: Human-readable description.
            data_view_id: Data view this filter is scoped to.
            definition: Filter rule as a CJA definition object.
                Example — members with claims > 2:
                {
                  "func": "segment",
                  "version": [1, 0, 0],
                  "container": {
                    "func": "container",
                    "context": "person",
                    "criteria": {
                      "func": "condition",
                      "col": {"func": "metric", "name": "metrics/claims"},
                      "pred": {"func": "GreaterThan", "val": {"func": "const", "val": 2}}
                    }
                  }
                }
        """
        try:
            body = {
                "name": name,
                "description": description,
                "rsid": data_view_id,
                "definition": definition,
            }
            return cja_post("/segments", body)
        except Exception as exc:
            return {"error": str(exc)}

    @mcp.tool()
    @track("cja_update_filter")
    def cja_update_filter(filter_id: str, updates: dict) -> dict:
        """Update an existing CJA filter (full replace).

        Args:
            filter_id: Filter ID to update.
            updates: Full filter definition object (same shape as create).
        """
        try:
            return cja_put(f"/segments/{filter_id}", updates)
        except Exception as exc:
            return {"error": str(exc)}

    @mcp.tool()
    @track("cja_delete_filter")
    def cja_delete_filter(filter_id: str) -> dict:
        """Delete a CJA filter.

        Args:
            filter_id: Filter ID to delete.
        """
        try:
            result = cja_delete(f"/segments/{filter_id}")
            return result or {"status": "deleted", "id": filter_id}
        except Exception as exc:
            return {"error": str(exc)}

    # ── Projects (Analysis Workspace) ─────────────────────────────────────────

    @mcp.tool()
    @track("cja_list_projects")
    def cja_list_projects(
        limit: int = 20,
        expansion: str = "",
    ) -> dict:
        """List CJA Workspace projects.

        Args:
            limit: Max records.
            expansion: Comma-separated fields to expand (e.g. 'definition,tags,shares').
        """
        try:
            params: dict = {"limit": limit}
            if expansion:
                params["expansion"] = expansion
            return cja_get("/projects", params=params)
        except Exception as exc:
            return {"error": str(exc)}

    @mcp.tool()
    @track("cja_get_project")
    def cja_get_project(project_id: str, expansion: str = "") -> dict:
        """Get a specific CJA Workspace project (including its panel/visualization JSON).

        Args:
            project_id: Project ID.
            expansion: Comma-separated fields to expand.
        """
        try:
            params = {"expansion": expansion} if expansion else {}
            return cja_get(f"/projects/{project_id}", params=params)
        except Exception as exc:
            return {"error": str(exc)}

    @mcp.tool()
    @track("cja_create_project")
    def cja_create_project(
        name: str,
        description: str,
        data_view_id: str,
        definition: dict,
    ) -> dict:
        """Create a CJA Workspace project.

        A project definition is a JSON tree of panels and visualizations.
        The minimal structure is:
        {
          "version": "32",
          "pages": [{
            "name": "Page 1",
            "panels": [{
              "type": "table",
              "name": "Freeform Table",
              "rows": [{"id": "dimension/daterangeday"}],
              "columns": [{"id": "metrics/visits"}]
            }]
          }]
        }

        Args:
            name: Project display name.
            description: Human-readable description.
            data_view_id: Default data view for the project.
            definition: Full project JSON (panels, visualizations, filters).
        """
        try:
            body = {
                "name": name,
                "description": description,
                "rsid": data_view_id,
                "definition": definition,
                "type": "project",
            }
            return cja_post("/projects", body)
        except Exception as exc:
            return {"error": str(exc)}

    @mcp.tool()
    @track("cja_update_project")
    def cja_update_project(project_id: str, updates: dict) -> dict:
        """Update an existing CJA Workspace project (full replace).

        Args:
            project_id: Project ID to update.
            updates: Full project definition object.
        """
        try:
            return cja_put(f"/projects/{project_id}", updates)
        except Exception as exc:
            return {"error": str(exc)}

    @mcp.tool()
    @track("cja_delete_project")
    def cja_delete_project(project_id: str) -> dict:
        """Delete a CJA Workspace project.

        Args:
            project_id: Project ID to delete.
        """
        try:
            result = cja_delete(f"/projects/{project_id}")
            return result or {"status": "deleted", "id": project_id}
        except Exception as exc:
            return {"error": str(exc)}

    # ── Annotations ───────────────────────────────────────────────────────────

    @mcp.tool()
    @track("cja_list_annotations")
    def cja_list_annotations(limit: int = 20, expansion: str = "") -> dict:
        """List CJA annotations.

        Args:
            limit: Max records.
            expansion: Comma-separated fields to expand.
        """
        try:
            params: dict = {"limit": limit}
            if expansion:
                params["expansion"] = expansion
            return cja_get("/annotations", params=params)
        except Exception as exc:
            return {"error": str(exc)}

    @mcp.tool()
    @track("cja_create_annotation")
    def cja_create_annotation(
        name: str,
        description: str,
        data_view_id: str,
        date_range: str,
        color: str = "STANDARD1",
        apply_to_all_reports: bool = False,
        metrics: list = [],
        dimensions: list = [],
    ) -> dict:
        """Create a CJA annotation marking a date range with a note.

        Args:
            name: Annotation label (shown in charts).
            description: Full note text.
            data_view_id: Data view to attach the annotation to.
            date_range: ISO 8601 date or range (e.g. '2024-06-01/2024-06-07').
            color: Badge color — one of STANDARD1 through STANDARD9.
            apply_to_all_reports: If true, shows across all projects.
            metrics: List of metric IDs to scope the annotation to.
            dimensions: List of dimension IDs to scope the annotation to.
        """
        try:
            body: dict = {
                "name": name,
                "description": description,
                "rsid": data_view_id,
                "dateRange": date_range,
                "color": color,
                "applyToAllReports": apply_to_all_reports,
            }
            if metrics:
                body["metrics"] = metrics
            if dimensions:
                body["dimensions"] = dimensions
            return cja_post("/annotations", body)
        except Exception as exc:
            return {"error": str(exc)}

    @mcp.tool()
    @track("cja_delete_annotation")
    def cja_delete_annotation(annotation_id: str) -> dict:
        """Delete a CJA annotation.

        Args:
            annotation_id: Annotation ID to delete.
        """
        try:
            result = cja_delete(f"/annotations/{annotation_id}")
            return result or {"status": "deleted", "id": annotation_id}
        except Exception as exc:
            return {"error": str(exc)}

    # ── Reports (Analytics Queries) ───────────────────────────────────────────

    @mcp.tool()
    @track("cja_run_report")
    def cja_run_report(
        data_view_id: str,
        date_range: str,
        metrics: list,
        dimension: str = "",
        filters: list = [],
        limit: int = 50,
        locale: str = "en_US",
    ) -> dict:
        """Run a CJA analytics report and return tabular results.

        Args:
            data_view_id: Data view to query (e.g. 'dv_abc123').
            date_range: ISO 8601 date range (e.g. '2024-01-01/2024-03-31').
            metrics: List of metric IDs to include (e.g. ['metrics/visits', 'metrics/orders']).
            dimension: Optional breakdown dimension ID (e.g. 'dimension/evar1').
                       Omit for a single totals row.
            filters: Optional list of filter/segment IDs to apply globally.
            limit: Max rows when a dimension is specified (default 50).
            locale: Locale for label resolution.

        Returns tabular data: rows × columns with dimension values and metric totals.
        """
        try:
            global_filters = [{"type": "dateRange", "dateRange": date_range}]
            for fid in filters:
                global_filters.append({"type": "segment", "segmentId": fid})

            body: dict = {
                "rsid": data_view_id,
                "globalFilters": global_filters,
                "metricContainer": {
                    "metrics": [{"columnId": i, "id": m} for i, m in enumerate(metrics)]
                },
                "settings": {"limit": limit, "locale": locale},
            }
            if dimension:
                body["dimension"] = dimension

            return cja_post("/reports", body)
        except Exception as exc:
            return {"error": str(exc)}
