# main.py

from confluent_kafka import Consumer, Producer
import json
import time
import signal
import sys
import pandas as pd

KAFKA_BROKER = "kafka:9092"
TOPIC_IN = "raw-data"
TOPIC_OUT = "processed-data"
GROUP_ID = "data-science-group"

# Graceful shutdown
running = True


def handle_sigint(sig, frame):
    global running
    print("🛑 Gracefully shutting down...")
    running = False


signal.signal(signal.SIGINT, handle_sigint)

# Kafka setup
consumer = Consumer({
    "bootstrap.servers": KAFKA_BROKER,
    "group.id": GROUP_ID,
    "auto.offset.reset": "earliest"
})

producer = Producer({"bootstrap.servers": KAFKA_BROKER})

# Processing function


def process_data(data: dict) -> dict:
    df = pd.DataFrame([data])
    df["result"] = df["value"] * 10  # 🔁 Example transformation
    return df.iloc[0].to_dict()

# Delivery report


def delivery_report(err, msg):
    if err is not None:
        print(f"❌ Delivery failed: {err}")
    else:
        print(f"✅ Sent to {msg.topic()} [{msg.partition()}]")

# Start consuming


def main():
    consumer.subscribe([TOPIC_IN])
    print(f"📡 Listening on topic '{TOPIC_IN}'...")

    while running:
        msg = consumer.poll(timeout=1.0)
        if msg is None:
            continue
        if msg.error():
            print(f"⚠️ Consumer error: {msg.error()}")
            continue

        try:
            data = json.loads(msg.value().decode("utf-8"))
            print(f"📥 Received: {data}")

            processed = process_data(data)
            print(f"🧠 Processed: {processed}")

            producer.produce(
                topic=TOPIC_OUT,
                value=json.dumps(processed),
                key=str(processed.get("id", "default")),
                callback=delivery_report
            )
            producer.flush()

        except Exception as e:
            print(f"🔥 Error processing message: {e}")

    consumer.close()


if __name__ == "__main__":
    main()
