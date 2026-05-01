import pandas as pd
import joblib
import os

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline

from src.pipeline import preprocessor


def train_model():
    df = pd.read_csv("data/students.csv")

    X = df.drop("passed", axis=1)
    y = df["passed"]

    # ✅ FIX: stratified split
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42,
        stratify=y
    )

    model = Pipeline([
        ("pre", preprocessor),
        ("clf", RandomForestClassifier(n_estimators=200, random_state=42))
    ])

    model.fit(X_train, y_train)

    os.makedirs("models", exist_ok=True)
    joblib.dump(model, "models/model.joblib")

    print("✅ Model trained & saved")

    return model, X_test, y_test