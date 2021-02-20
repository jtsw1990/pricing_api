import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder

class TechnicalRiskModel:
    
    def __init__(self):
        pass
    
    def data_reader(self, path):
        self._path = path
        return pd.read_csv(self._path)

    def data_preprocesser(self, df, rating_factors):
        self._rating_factors_col = rating_factors
        self._claims_col = df.columns[-1]
        self._num_features = list(df[self._rating_factors_col].select_dtypes(include=["int64", "float64"]).columns)
        self._cat_features = [col for col in self._rating_factors_col if col not in self._num_features]
        self._preprocesser = ColumnTransformer(
                transformers = [
                    ("numerical", "passthrough", self._num_features),
                    ("categorical", OneHotEncoder(sparse=False, handle_unknown="ignore"), self._cat_features)
                    ]
                )
        X_train, X_test, y_train, y_test = train_test_split(
                df[self._rating_factors_col],
                df[claims_col],
                test_size=0.2,
                random_state=123
                )
        ohe_categories = preprcesser.fit(X_train).named_transformers_["categorical"].categories_
        ohe_categories_concat = [f"{col}_{val}" for col, val in zip(self._cat_features, ohe_categories) for val in vals]
        self._rating_factors_encoded = num_features + ohe_categories_concat
        return X_train, X_test, y_train, y_test, self._rating_factors_encoded


    def train_tech_model(self, data):
        pass

    def score_tech_model(self, pricing_call):
        return 50

