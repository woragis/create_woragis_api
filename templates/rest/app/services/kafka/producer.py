from confluent_kafka import Producer
import json

producer = Producer({'bootstrap.servers': 'localhost:9092'})


def send_event(topic: str, payload: dict):
    producer.produce(topic, value=json.dumps(payload))
    producer.flush()
