from fastapi import FastAPI
import joblib

app = FastAPI()

model = joblib.load("models/model.joblib")


@app.get("/")
def home():
    return {"message": "API Running"}


@app.post("/predict")
def predict(data: dict):
    pred = model.predict([data])[0]

    return {
        "prediction": int(pred),
        "result": "Pass" if pred == 1 else "Fail"
    }