# kafka-assert

Kafka consumer and Kafka message assertions for testing environments.

Disclaimer: this is a work in progress project, stay tuned for updates.

## Getting Started


```python

kafka_consumer = KafkaConsumer(topics=['orders-topic'])

msg = kafka_consumer.consume_one(timeout=8.0)

assert_json_kafka_message(msg, event_type='ProductAdded')

```
