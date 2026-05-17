from kafka import KafkaConsumer
import json
import os
import numpy as np
import joblib
import pandas as pd
from kafka import KafkaProducer
# Load trained model
model = joblib.load("models/random_forest_model.pkl")

# Load scaler
scaler = joblib.load("models/scaler.pkl")
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

LOG_FILE = os.path.join(BASE_DIR, "predictions.json")
# Kafka Consumer
consumer = KafkaConsumer(
    "transactions",
    bootstrap_servers="redpanda:9092",
    value_deserializer=lambda x: json.loads(x.decode("utf-8"))
)
alert_producer = KafkaProducer(
    bootstrap_servers="redpanda:9092",
    value_serializer=lambda v: json.dumps(v).encode("utf-8")
)
print("Fraud Detection Consumer Started...")

for message in consumer:

    transaction = message.value

    print("\nIncoming Transaction:")
    print(transaction)

    # Convert transaction into DataFrame
    df = pd.DataFrame([transaction])

    # Ensure correct feature order
    feature_order = [
        "Time",
        "V1","V2","V3","V4","V5","V6","V7","V8","V9","V10",
        "V11","V12","V13","V14","V15","V16","V17","V18",
        "V19","V20","V21","V22","V23","V24","V25","V26",
        "V27","V28",
        "Amount"
    ]

    df = df[feature_order]

    # Scale features
    scaled_features = scaler.transform(df)

    # Predict fraud probability
    probability = model.predict_proba(scaled_features)[0][1]

    # Final prediction
    prediction = "FRAUD" if probability > 0.5 else "NORMAL"

    if prediction == "FRAUD":

     alert = {
        "message": "Fraudulent transaction detected",
        "probability": float(probability),
        "amount": transaction["Amount"]
     }

     alert_producer.send(
        "fraud_alerts",
        value=alert
     )

     print("FRAUD ALERT EMITTED")

    print(f"Fraud Probability: {probability:.4f}")
    print(f"Prediction: {prediction}")

    result = {
    "probability": float(probability),
    "prediction": prediction,
    "amount": transaction["Amount"]
   }

    if os.path.exists(LOG_FILE):

     with open(LOG_FILE, "r") as f:
        data = json.load(f)

    else:
      data = []

    data.append(result)

   # Keep only latest 100 predictions
    data = data[-100:]

    with open(LOG_FILE, "w") as f:
     json.dump(data, f, indent=2)   


 