from flask_restful import Resource


class HealthResource(Resource):

    def get(self):
        """
        check health of server(running or not)
        ---
        tags:
          - "Health"
        responses:
          200:
            description: server is running
        """
        return "server is up and running"
