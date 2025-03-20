import os
from mongoDBService.core import MongoDBService
from rabbitMQService.core import RabbitMQConsumer
from rabbitMQService.entities import QueueMessageFlatFiles
from dataDriftService.core import DataDriftService
import pandas as pd
import json

user_name = os.getenv("RABBITMQ_USERNAME")
password = os.getenv("RABBITMQ_PASSWORD")
host = os.getenv("RABBITMQ_HOST")
mongo_user = os.getenv("MONGO_USER")
mongo_password = os.getenv("MONGO_PASSWORD")
mongo_host = os.getenv("MONGO_HOST")
mongo_db = os.getenv("MONGO_DB")
mongo_collection = os.getenv("MONGO_COLLECTION")
port = 5672


def callback(ch, method, properties, body):
    message = json.loads(body.decode())
    message = QueueMessageFlatFiles(**message)
    print(f" [x] Received {message}")
    reference_data = pd.read_csv(message.reference_data_path)
    current_data = pd.read_csv(message.current_data_path)
    drift_service = DataDriftService(
        model_id=message.model_id,
        reference_data=reference_data,
        current_data=current_data,
    )
    drift_report = drift_service.get_report_html()
    db_service = MongoDBService(
        host=mongo_host,
        user=None,
        password=None,
        dbname=mongo_db,
        collection=mongo_collection,
    )
    db_service.insert_drift_report_html(drift_report)
    print(" [x] Done")
    ch.basic_ack(delivery_tag=method.delivery_tag)


class DataDriftWorkerHtmlFlatFile:
    def run(self):
        consumer = RabbitMQConsumer(
            host=host, port=port, username=user_name, password=password
        )
        consumer.connect_to_queue(queue_name="data_drift")
        consumer.consume(callback)


class DataQualityWorker:
    pass
