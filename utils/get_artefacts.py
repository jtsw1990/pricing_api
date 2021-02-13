import json

def get_schema():
	with open(r"schema/travel_contract.json") as f:
		schema = json.load(f)
	return schema
