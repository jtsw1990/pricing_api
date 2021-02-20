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
        X_train, X_test, y_train, y_test = train_test_split(
                df[self._rating_factors_col],
                df[self._claims_col],
                test_size=0.2,
                random_state=123
                )
        ohe_categories = self._preprocessor.fit(X_train).named_transformers_["categorical"].categories_
        ohe_categories_concat = [f"{col}_{val}" for col, vals in zip(self._cat_features, ohe_categories) for val in vals]
        self._rating_factors_encoded = self._num_features + ohe_categories_concat
        self._preprocessor.fit(X_train)
        X_train = self._preprocessor.transform(X_train)
        X_test = self._preprocessor.transform(X_test)
        return X_train, X_test, y_train, y_test, self._rating_factors_encoded


    def train_tech_model(self, X_train, y_train):
        model = LinearRegression.fit(X_train, y_train)
        # TODO: add some output logs and statistics
        filename = "latest_model.sav"
        pickle.dump(model, open(filename, "wb"))

    def score_tech_model(self, pricing_call, pricing_rule):
        return 50


if __name__ == "__main__":
   src = TechnicalRiskModel()
   df = src.data_reader(r"C:\Users\jtsw1\Desktop\projects\pricing_api\data\pif_data.csv")
   X_train, X_test, y_train, y_test, col_names = src.data_preprocessor(df, ["destination_region", "ski_flag", "gender_code", "date_of_birth"])


