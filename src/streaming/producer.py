from kafka import KafkaProducer
import json
import time
import random

producer = KafkaProducer(
    bootstrap_servers='redpanda:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

topic = "transactions"

while True:

    is_fraud = random.random() < 0.1

    if is_fraud:

     transaction = {
        "Time": random.randint(1000, 50000),

        "V1": random.uniform(-15, -5),
        "V2": random.uniform(5, 15),
        "V3": random.uniform(-15, -5),
        "V4": random.uniform(5, 15),
        "V5": random.uniform(-15, -5),
        "V6": random.uniform(-15, -5),
        "V7": random.uniform(-15, -5),
        "V8": random.uniform(5, 15),
        "V9": random.uniform(-15, -5),
        "V10": random.uniform(-15, -5),
        "V11": random.uniform(5, 15),
        "V12": random.uniform(-15, -5),
        "V13": random.uniform(-5, 5),
        "V14": random.uniform(-15, -5),
        "V15": random.uniform(-5, 5),
        "V16": random.uniform(-15, -5),
        "V17": random.uniform(-15, -5),
        "V18": random.uniform(-15, -5),
        "V19": random.uniform(-5, 5),
        "V20": random.uniform(-5, 5),
        "V21": random.uniform(5, 15),
        "V22": random.uniform(-5, 5),
        "V23": random.uniform(-5, 5),
        "V24": random.uniform(-5, 5),
        "V25": random.uniform(-5, 5),
        "V26": random.uniform(-5, 5),
        "V27": random.uniform(5, 15),
        "V28": random.uniform(5, 15),

        "Amount": round(random.uniform(2000, 10000), 2)
    }

    else:

     transaction = {
        "Time": random.randint(1000, 50000),

        "V1": random.uniform(-3, 3),
        "V2": random.uniform(-3, 3),
        "V3": random.uniform(-3, 3),
        "V4": random.uniform(-3, 3),
        "V5": random.uniform(-3, 3),
        "V6": random.uniform(-3, 3),
        "V7": random.uniform(-3, 3),
        "V8": random.uniform(-3, 3),
        "V9": random.uniform(-3, 3),
        "V10": random.uniform(-3, 3),
        "V11": random.uniform(-3, 3),
        "V12": random.uniform(-3, 3),
        "V13": random.uniform(-3, 3),
        "V14": random.uniform(-3, 3),
        "V15": random.uniform(-3, 3),
        "V16": random.uniform(-3, 3),
        "V17": random.uniform(-3, 3),
        "V18": random.uniform(-3, 3),
        "V19": random.uniform(-3, 3),
        "V20": random.uniform(-3, 3),
        "V21": random.uniform(-3, 3),
        "V22": random.uniform(-3, 3),
        "V23": random.uniform(-3, 3),
        "V24": random.uniform(-3, 3),
        "V25": random.uniform(-3, 3),
        "V26": random.uniform(-3, 3),
        "V27": random.uniform(-3, 3),
        "V28": random.uniform(-3, 3),

        "Amount": round(random.uniform(10, 2000), 2)
    }

    producer.send(topic, value=transaction)

    print("Transaction Sent:", transaction)

    time.sleep(2)