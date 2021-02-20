from flask import Flask
from flask_restful import Resource, Api, reqparse
from risk_model.tech_model import TechnicalRiskModel
from utils.get_artefacts import get_schema
from utils.parse_call import parse_pricing_call
import os

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

        contract = get_schema()
        request = contract["request"]
        parser = reqparse.RequestParser()
        {parser.add_argument(key, required=False) for (key, value) in request.items()}
        args = parser.parse_args()
        mapped_args = parse_pricing_call(args, os.path.join(os.getcwd(), "mapping_tables/travel_mapping.csv"))
        # TODO: link in tech model
        
        pricing_response = TechnicalRiskModel().score_tech_model(mapped_args, os.path.join(os.getcwd(), "risk_model/latest_model.sav"))
        

        return {"placeholder_premium": pricing_response}, 200

api.add_resource(PricingAPI, "/pricing")
api.add_resource(Status, "/healthcheck")

if __name__ == "__main__":
    app.run()
