from flask import request

from flask_restful import Resource

from app.service.status import TransStatusService


class TransStatusResource(Resource):

    def patch(self, trans_id):
        """
        update transaction status
        ---
        tags:
          - "Transaction"
        summary: update transaction status for protectPe transaction
        consumes:
          - "application/json"
        produces:
          - "application/json"
        parameters:
          - name: "trans_id"
            in: "path"
            description: "trans_id"
            required: true
            type: "string"
          - in: "body"
            name: "body"
            description: "update Transaction status(APPROVE/DENY) that needs to be added to the protectpe account"
            required: true
            schema:
              $ref: "#/definitions/Status"
        responses:
          200:
            description: created a new transaction
        definitions:
          Status:
            type: "object"
            properties:
              status:
                type: "string"
                required: true
            example: {
                        "status": "APPROVE"
                    }
        """
        return TransStatusService.update_trans_status(trans_id, request.json)
