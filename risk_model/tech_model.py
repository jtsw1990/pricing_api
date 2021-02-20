import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.linear_model import LinearRegression
import numpy
import pickle



class TechnicalRiskModel:
    
    def __init__(self):
        pass
    
    def data_reader(self, path):
        self._path = path
        return pd.read_csv(self._path)

    def data_preprocessor(self, df, rating_factors):
        self._rating_factors_col = rating_factors
        self._claims_col = df.columns[-1]
        self._num_features = list(df[self._rating_factors_col].select_dtypes(include=["int64", "float64"]).columns)
        self._cat_features = [col for col in self._rating_factors_col if col not in self._num_features]
        self._preprocessor = ColumnTransformer(
                transformers = [
                    ("numerical", "passthrough", self._num_features),
                    ("categorical", OneHotEncoder(sparse=False, handle_unknown="ignore"), self._cat_features)
                    ]
                )
        X, y = df[self._rating_factors_col], df[self._claims_col]
        
        ohe_categories = self._preprocessor.fit(X).named_transformers_["categorical"].categories_
        ohe_categories_concat = [f"{col}_{val}" for col, vals in zip(self._cat_features, ohe_categories) for val in vals]
        self._rating_factors_encoded = self._num_features + ohe_categories_concat
        self._preprocessor.fit(X)
        X = self._preprocessor.transform(X)
        return X, y, self._rating_factors_encoded


    def train_tech_model(self, X, y):
        X_train, X_test, y_train, y_test = train_test_split(
            X,
            y,
            test_size=0.2,
            random_state=123
        )
        self.model = LinearRegression().fit(X_train, y_train)
        # TODO: add some output logs and statistics
        # TODO: add timestamps and string formatting in output
        filename = "latest_model.sav"
        pickle.dump(self.model, open(filename, "wb"))

    def score_tech_model(self, pricing_call, pricing_rule):
        loaded_model = pickle.load(open(pricing_rule, "rb"))
        pricing_call_parsed = self._preprocessor.transform(pd.DataFrame(pricing_call, index=[0]))
   
        return loaded_model.predict(pricing_call_parsed)[0]


if __name__ == "__main__":
    import os
    import json

    src = TechnicalRiskModel()
    df = src.data_reader(r"C:\Users\jtsw1\Desktop\projects\pricing_api\data\pif_data.csv")
    X, y, col_names = src.data_preprocessor(df, ["destination_region", "ski_flag", "gender_code", "date_of_birth"])
    src.train_tech_model(X, y)
    with open(r"C:\Users\jtsw1\Desktop\projects\pricing_api\data\sample_travel_pricing_call.json") as f:
        call = json.load(f)    
    
    mapping_table = pd.read_csv(r"C:\Users\jtsw1\Desktop\projects\pricing_api\mapping_tables\travel_mapping.csv")
    mapping_dict = dict(zip(mapping_table["global_variable"], mapping_table["data_column"]))
    call_mapped = {mapping_dict[key]: value for (key, value) in call.items()}
    premium = src.score_tech_model(call_mapped, "latest_model.sav")

