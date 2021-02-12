from flask import Flask
from flask_restful import Resource, Api, reqparse


app = Flask(__name__)
api = Api(app)

class Status(Resource):
    # Endpoint for getting server status
    def get(self):
        return {"Message": "Hello there"}, 200


class PricingAPI(Resource):
    # Insert methods here for GET/POST/DELETE ecti.

    def get(self)
        return {"Schema": "Placeholder"}, 200

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("TestingField", required=True)

        args = parser.parse_args()
        # import model

        # reformat into JSON output
        return {"Reporting parameters": "Placeholder"}, 200

api.add_resource("PricingAPI", "/pricing")
api.add_resource("Status", "/healthcheck")
