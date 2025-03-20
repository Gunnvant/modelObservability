from rabbitMQService.core import RabbitMQProducer
from dataDriftService.entitites import QueueMessageFlatFiles
import os
import json

user_name = os.getenv("RABBITMQ_USERNAME")
password = os.getenv("RABBITMQ_PASSWORD")
host = os.getenv("RABBITMQ_HOST")
port = 5672

message = QueueMessageFlatFiles(
    model_id="123",
    reference_data_path="./sample_data/benchmark_large.csv",
    current_data_path="./sample_data/benchmark_large.csv",
)
message_str = json.dumps(message.model_dump())
print(type(message_str))

producer = RabbitMQProducer(host=host, port=port, username=user_name, password=password)
producer.connect_to_queue(queue_name="data_drift")
producer.publish(message=message_str, routing_key="data_drift")
producer.close()
