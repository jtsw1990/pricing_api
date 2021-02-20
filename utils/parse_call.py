import json
import pandas as pd

def parse_pricing_call(json_input, mapping_table):
    call = json_input
    # with open(json_input) as f:
    #    call = json.load(f)

    mapping_table = pd.read_csv(mapping_table)
    mapping_dict = dict(zip(mapping_table["global_variable"], mapping_table["data_column"]))
    call_mapped = {mapping_dict[key]: value for (key, value) in call.items()}

    return call_mapped

if __name__ == "__main__":

   call_mapped = parse_pricing_call(r"C:\Users\jtsw1\Desktop\projects\pricing_api\data\sample_travel_pricing_call.json", r"C:\Users\jtsw1\Desktop\projects\pricing_api\mapping_tables\travel_mapping.csv")


