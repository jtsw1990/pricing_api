from flask import Flask
from flask_restful import Resource, Api, reqparse
from risk_model.tech_model import TechnicalRiskModel
from utils.get_artefacts import get_schema

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
        #parser = reqparse.RequestParser()
        #parser.add_argument("TestingField", required=True)

        #args = parser.parse_args()
        
        # reformat into JSON output
        model = TechnicalRiskModel()
        price = model.placeholder_tech_price()
        return {"placeholder_premium": price}, 200

api.add_resource(PricingAPI, "/pricing")
api.add_resource(Status, "/healthcheck")

if __name__ == "__main__":
    app.run()
