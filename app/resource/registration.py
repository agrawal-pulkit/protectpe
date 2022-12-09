from flask import request

from flask_restful import Resource

from app.service.registration import RegistrationService


class RegistrationResource(Resource):

    def get(self):
        """
        get all the registration
        ---
        tags:
          - "Registration"
        summary: get all registration
        parameters:
          - name: "primary_owner"
            in: "query"
            description: "get all protectPe registered users by primary owner number/upi_id"
            type: "string"
        responses:
          200:
            description: Get all registrations.
        """

        return RegistrationService.get_all_registration()

    def post(self):
        """
        add/register a new protectPe user
        ---
        tags:
          - "Registration"
        summary: add/register a new protectPe user
        consumes:
          - "application/json"
        produces:
          - "application/json"
        parameters:
          - in: "body"
            name: "body"
            description: "Registration object that needs to be added to the protectpe account"
            required: true
            schema:
              $ref: "#/definitions/Registration"
        responses:
          200:
            description: created a new registration
        definitions:
          Registration:
            type: "object"
            properties:
              phone_number:
                type: "string"
                required: true
              primary_owner:
                type: "string"
              description:
                type: "string"
                required: true
              regular_limit:
                type: "integer"
                required: true
              max_limit:
                type: "integer"
                required: true
            example: {
                        "phone_number": "9206255529",
                        "primary_owner": "9206255525",
                        "description": "kid",
                        "regular_limit": 100,
                        "max_limit": 1000
                    }
        """

        return RegistrationService.register_protectpe(request.json)


class RegistrationUpdateResource(Resource):

    def patch(self, phone_number):
        """
        update registration data(ex: verification_status/is_active)
        ---
        tags:
          - "Registration"
        summary: update registration  status for protectPe registration
        consumes:
          - "application/json"
        produces:
          - "application/json"
        parameters:
          - name: "phone_number"
            in: "path"
            description: "phone number of protectpe"
            required: true
            type: "string"
          - in: "body"
            name: "body"
            description: "update Registration"
            required: true
            schema:
              $ref: "#/definitions/UpdateRegister"
        responses:
          200:
            description: created a new registration 
        definitions:
          UpdateRegister:
            type: "object"
            properties:
              status:
                type: "string"
                required: true
            example: {
                        "verification_status": "COMPLETED"
                    }
        """
        return RegistrationService.update_reg_status(phone_number, request.json)