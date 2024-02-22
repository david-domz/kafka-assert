# Kafka-Assert

Kafka consumer and Kafka message assertions for testing environments.

## Getting Started


```python
from kafka_assert import KafkaConsumer, assert_kafka_message

kafka_consumer = KafkaConsumer(topics=['orders-topic'])

msg = kafka_consumer.consume_one(timeout=8.0)

assert_kafka_message(msg, event_type='ProductAdded')
```
