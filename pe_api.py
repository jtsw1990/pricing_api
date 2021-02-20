from flask import Flask
from flask_restful import Resource, Api, reqparse
from risk_model.tech_model import TechnicalRiskModel
from utils.get_artefacts import get_schema
from utils.parse_call import parse_pricing_call

app = Flask(__name__)
api = Api(app)

class Status(Resource):
    # Endpoint for getting server status
    def get(self):
        return {"Message": "Hello there"}, 200


class PricingAPI(Resource):
    # Insert methods here for GET/POST/DELETE ecti.
	
		
	
    def get(self):
        return get_schema(), 200

    def post(self):
        # TODO: read in contract + reqparser
        #parser = reqparse.RequestParser()
        #parser.add_argument("TestingField", required=True)

        #args = parser.parse_args()
        
        # TODO: link in tech model

        return {"placeholder_premium": price}, 200

api.add_resource(PricingAPI, "/pricing")
api.add_resource(Status, "/healthcheck")

if __name__ == "__main__":
    app.run()
