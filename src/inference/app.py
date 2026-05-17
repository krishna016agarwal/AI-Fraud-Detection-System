from fastapi import FastAPI
import joblib
import numpy as np

app = FastAPI()

# Load trained model
model = joblib.load("../../models/xgboost_model.pkl")

# Load scaler
scaler = joblib.load("../../models/scaler.pkl")


@app.get("/")
def home():
    return {"message": "Fraud Detection API Running"}


@app.post("/predict")
def predict(data: dict):

    features = np.array(list(data.values())).reshape(1, -1)

    scaled_features = scaler.transform(features)

    probability = model.predict_proba(scaled_features)[0][1]

    prediction = int(probability > 0.5)

    return {
        "fraud_probability": float(probability),
        "prediction": prediction
    }