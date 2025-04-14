from confluent_kafka import Consumer
import json

conf = {
    'bootstrap.servers': 'localhost:9092',
    'group.id': 'dashboard-consumers',
    'auto.offset.reset': 'earliest'
}

consumer = Consumer(conf)
consumer.subscribe(['metrics'])


def run_consumer():
    while True:
        msg = consumer.poll(1.0)
        if msg is None:
            continue
        if msg.error():
            print("Error: ", msg.error())
            continue
        data = json.loads(msg.value().decode('utf-8'))
        print("Received metric:", data)
        # Do something: push via socket, save to DB, call LangChain
