import sys

if sys.version_info >= (3, 12, 0):
    import six
    sys.modules['kafka.vendor.six.moves'] = six.moves


import json

from kafka import KafkaConsumer


def json_deserializer(data):
    return json.loads(data.decode("utf-8"))


consumer = KafkaConsumer(
    "test-topic",
    bootstrap_servers=["localhost:9092"],
    enable_auto_commit=True,
    group_id="my-group",
    value_deserializer=json_deserializer,
    auto_offset_reset="earliest"
)

for message in consumer:
    print('='*20)
    print(f"Received: {message.value}")
