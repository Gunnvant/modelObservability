from rabbitMQService.core import RabbitMQConsumer
import os

user_name = os.getenv("RABBITMQ_USERNAME")
password = os.getenv("RABBITMQ_PASSWORD")
host = os.getenv("RABBITMQ_HOST")
port = 5672

rbmq = RabbitMQConsumer(host, port, user_name, password)
rbmq.connect_to_queue(queue_name="test")


def callback(ch, method, properties, body):
    print(f"message received: {body.decode()}")
    ch.basic_ack(delivery_tag=method.delivery_tag)


rbmq.consume(callback)
