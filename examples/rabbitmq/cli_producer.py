from rabbitMQService.core import RabbitMQProducer
import os

user_name = os.getenv("RABBITMQ_USERNAME")
password = os.getenv("RABBITMQ_PASSWORD")
host = os.getenv("RABBITMQ_HOST")
port = 5672

rbmq = RabbitMQProducer(host, port, user_name, password)
rbmq.connect_to_queue(queue_name="test")
rbmq.publish(message="test", routing_key="test")
