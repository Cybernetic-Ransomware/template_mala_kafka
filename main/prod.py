import sys

if sys.version_info >= (3, 12, 0):
    import six
    sys.modules['kafka.vendor.six.moves'] = six.moves


import json

from kafka import KafkaProducer


def json_serializer(data):
    return json.dumps(data).encode("utf-8")


kafka_prod = KafkaProducer(
    bootstrap_servers=["localhost:9092"],
    value_serializer=json_serializer
)

topic = "test-topic"
for i in range(10):
    message = {"number": i}
    kafka_prod.send(topic, message)


kafka_prod.flush()
kafka_prod.close()

print('Sending: DONE')
