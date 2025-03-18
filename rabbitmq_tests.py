import pytest
import rabbitMQService.core as core
import os

user_name = os.getenv("RABBITMQ_USERNAME")
password = os.getenv("RABBITMQ_PASSWORD")
host = os.getenv("RABBITMQ_HOST")
port = 5672


def test_get_rabbitmq_connection():
    producer = core.RabbitMQProducer(host, port, user_name, password)
    producer.connect_to_queue(queue_name="test")
    assert producer.channel is not None
    producer.close()

    consumer = core.RabbitMQConsumer(host, port, user_name, password)
    consumer.connect_to_queue(queue_name="test")
    assert consumer.channel is not None
    consumer.close()


def test_publish_message():
    rbmq = core.RabbitMQProducer(host, port, user_name, password)
    rbmq.connect_to_queue(queue_name="test")
    try:
        rbmq.publish("test", "test")
        published = True
    except:
        published = False
    assert published
    rbmq.close()


def test_bind_and_consume():
    rbmq = core.RabbitMQConsumer(host, port, user_name, password)
    rbmq.connect_to_queue(queue_name="test")

    def callback(ch, method, properties, body):
        print(f"message received: {body.decode()}")
        assert body.decode() == "test"
        ch.basic_ack(delivery_tag=method.delivery_tag)
        ch.stop_consuming()

    rbmq.consume(callback)
    rbmq.close()
