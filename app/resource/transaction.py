from flask import request

from flask_restful import Resource

from app.service.transaction import TransactionService


class TransactionResource(Resource):

    def get(self):
        """
        get all the transaction
        ---
        tags:
          - "Transaction"
        summary: get all transaction
        parameters:
          - name: "user_id"
            in: "query"
            description: "get all protectPe transactions by user_id(kid phonepe number)"
            type: "string"
          - name: "primary_owner"
            in: "query"
            description: "get all protectPe transactions by primary_owner(parent)"
            type: "string"
        responses:
          200:
            description: Get all transactions.
        """
        return TransactionService.get_all_transaction()

    def post(self):
        """
        add/register a new protectPe transaction
        ---
        tags:
          - "Transaction"
        summary: add/register a new protectPe transaction
        consumes:
          - "application/json"
        produces:
          - "application/json"
        parameters:
          - in: "body"
            name: "body"
            description: "Transaction object that needs to be added to the protectpe account"
            required: true
            schema:
              $ref: "#/definitions/Transaction"
        responses:
          200:
            description: created a new transaction
        definitions:
          Transaction:
            type: "object"
            properties:
              user_id:
                type: "string"
                required: true
              merchant_upi_id:
                type: "string"
                required: true
              transaction_amount:
                type: "integer"
                required: true
            example: {
                    "user_id": "9206255527",
                    "merchant_upi_id": "9206255221@upi",
                    "transaction_amount": 20000
                }
        """
        return TransactionService.create_transaction(request.json)
