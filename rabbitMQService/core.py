import inspect
import pika
from typing import Callable
from abc import ABC, abstractmethod


class RabbitMQServiceInterface(ABC):
    @abstractmethod
    def connect_to_queue(self):
        pass

    @abstractmethod
    def consume(self):
        pass

    @abstractmethod
    def publish(self):
        pass

    @abstractmethod
    def close(self):
        pass


class RabbitMQProducer(RabbitMQServiceInterface):
    def __init__(self, host: str, port: int, username: str, password: str):
        self.host = host
        self.port = port
        self.username = username
        self.password = password

    def connect_to_queue(self, queue_name: str):
        credentials = pika.PlainCredentials(self.username, self.password)
        parameters = pika.ConnectionParameters(self.host, self.port, "/", credentials)
        self.connection = pika.BlockingConnection(parameters)
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue=queue_name, durable=True)
        self.queue_name = queue_name
        return self

    def publish(self, message: str, routing_key: str):
        if self.channel is None:
            raise Exception("RabbitMQ channel not initialized")
        if self.queue_name is None:
            raise Exception("RabbitMQ queue not initialized")

        self.channel.basic_publish(
            exchange="",
            routing_key=routing_key,
            body=message,
            properties=pika.BasicProperties(delivery_mode=pika.DeliveryMode.Persistent),
        )
        self.channel.close()
        return self

    def close(self):
        self.connection.close()
        return self

    def consume(self):
        raise NotImplementedError(
            "This method is not implemented in the producer class"
        )


class RabbitMQConsumer(RabbitMQServiceInterface):
    def __init__(self, host: str, port: int, username: str, password: str):
        self.host = host
        self.port = port
        self.username = username
        self.password = password

    def connect_to_queue(self, queue_name: str):
        credentials = pika.PlainCredentials(self.username, self.password)
        parameters = pika.ConnectionParameters(self.host, self.port, "/", credentials)
        self.connection = pika.BlockingConnection(parameters)
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue=queue_name, durable=True)
        self.queue_name = queue_name

    def consume(self, callback: Callable):
        if self.channel is None:
            raise Exception("RabbitMQ channel not initialized")
        if self.queue_name is None:
            raise Exception("RabbitMQ queue not initialized")
        source_code = inspect.getsource(callback)
        if "basic_ack" not in source_code:
            raise ValueError(
                "Callback function must acknowledge messages using the 'basic_ack' method"
            )
        self.channel.basic_qos(prefetch_count=1)
        self.channel.basic_consume(
            queue=self.queue_name, on_message_callback=callback, auto_ack=False
        )
        self.channel.start_consuming()

    def close(self):
        self.connection.close()
        return self

    def publish(self):
        raise NotImplementedError(
            "This method is not implemented in the consumer class"
        )
