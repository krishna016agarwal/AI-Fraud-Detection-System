from kafka import KafkaConsumer
import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

ALERT_FILE = os.path.join(
    BASE_DIR,
    "alerts.json"
)

consumer = KafkaConsumer(
    "fraud_alerts",
    bootstrap_servers="redpanda:9092",
    value_deserializer=lambda x: json.loads(x.decode("utf-8")),
)

print("Fraud Alert Service Started...")

for message in consumer:

    alert = message.value

    print("\nFRAUD ALERT RECEIVED")

    alert_data = {
        "message": alert["message"],
        "probability": alert["probability"],
        "amount": alert["amount"],
    }

    # Load old alerts
    if os.path.exists(ALERT_FILE):

        try:
            with open(ALERT_FILE, "r") as f:
                alerts = json.load(f)

        except:
            alerts = []

    else:
        alerts = []

    # Add new alert
    alerts.append(alert_data)

    # Keep latest 20 alerts only
    alerts = alerts[-5:]

    # Save alerts
    with open(ALERT_FILE, "w") as f:
        json.dump(alerts, f, indent=2)

    print("ALERT STORED")