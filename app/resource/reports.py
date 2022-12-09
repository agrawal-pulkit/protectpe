from flask_restful import Resource

from app.service.reports import ReportService


class ReportResource(Resource):

    def get(self, primary_owner):
        """
        get all aggregated data for owner
        ---
        tags:
          - "Report"
        summary: get aggregated data for owner
        parameters:
          - name: "primary_owner"
            in: "path"
            description: "get aggregated data for aall protectpe users for primary owner"
            required: true
            type: "string"
        responses:
          200:
            description: get aggregated data for owner
        """
        return ReportService.get_agg_data(primary_owner)