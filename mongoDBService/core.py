from __future__ import annotations
import urllib.parse
from pymongo import MongoClient
from abc import ABC, abstractmethod
from .entities import DriftReportHtml
from typing_extensions import Self
from datetime import datetime


class MongoDBInterface(ABC):
    @abstractmethod
    def init_client(self):
        pass

    def insert_drift_report_html(self):
        pass

    def close_client(self):
        pass

    def get_drift_reports_by_model_id(self):
        pass

    def get_drift_reports_by_datetime_range(self):
        pass

    def get_drift_reports_by_model_id_and_datetime_range(self):
        pass

    def get_all_drift_reports(self):
        pass

    def delete_drift_reports_by_model_id(self):
        pass

    def delete_drift_reports_by_datetime_range(self):
        pass

    def delete_drift_reports_by_model_id_and_datetime_range(self):
        pass

    def delete_all_drift_reports(self):
        pass


class MongoDBService(MongoDBInterface):
    def __init__(
        self,
        host: str,
        user: str | None,
        password: str | None,
        collection: str,
        dbname: str,
    ):
        self.host = host
        self.user = user
        self.password = password
        self.dbname = dbname
        self.collection = collection

    def init_client(self) -> Self:
        if self.user is not None and self.password is not None:
            user = urllib.parse.quote_plus(self.user)
            password = urllib.parse.quote_plus(self.password)
            conn_string = f"mongodb://{user}:{password}@{self.host}"
        else:
            conn_string = f"mongodb://{self.host}"
        self.client = MongoClient(conn_string)
        return self

    def insert_drift_report_html(self, report: DriftReportHtml) -> Self:
        self.init_client()
        db = self.client[self.dbname]
        col = db[self.collection]
        try:
            col.insert_one(report.model_dump())
        except Exception as e:
            print(f"Error inserting drift report: {e}")
        finally:
            self.client.close()
        return self

    def close_client(self):
        if self.client is not None:
            self.client.close()
        else:
            raise Exception("Client is not initialized, can't be closed")

    def get_drift_reports_by_model_id(self, model_id: str) -> list[DriftReportHtml]:
        self.init_client()
        db = self.client[self.dbname]
        col = db[self.collection]
        reports = []
        try:
            results = col.find({"model_id": model_id})
            for result in results:
                reports.append(DriftReportHtml(**result))
        except Exception as e:
            print(f"Error getting drift reports by model id: {e}")
        finally:
            self.client.close()
        return reports

    def get_drift_reports_by_datetime_range(
        self, start: datetime, end: datetime
    ) -> list[DriftReportHtml]:
        self.init_client()
        db = self.client[self.dbname]
        col = db[self.collection]
        reports = []
        try:
            results = col.find({"timestamp": {"$gte": start, "$lte": end}})
            for result in results:
                reports.append(DriftReportHtml(**result))
        except Exception as e:
            print(f"Error getting drift reports by datetime range: {e}")
        finally:
            self.client.close()
        return reports

    def get_drift_reports_by_model_id_and_datetime_range(
        self, model_id: str, start: datetime, end: datetime
    ) -> list[DriftReportHtml]:
        self.init_client()
        db = self.client[self.dbname]
        col = db[self.collection]
        reports = []
        try:
            results = col.find(
                {"model_id": model_id, "timestamp": {"$gte": start, "$lte": end}}
            )
            for result in results:
                reports.append(DriftReportHtml(**result))
        except Exception as e:
            print(f"Error getting drift reports by model id and datetime range: {e}")
        finally:
            self.client.close()
        return reports

    def get_all_drift_reports(self):
        self.init_client()
        db = self.client[self.dbname]
        col = db[self.collection]
        reports = []
        try:
            results = col.find()
            for result in results:
                reports.append(DriftReportHtml(**result))
        except Exception as e:
            print(f"Error getting all drift reports: {e}")
        finally:
            self.client.close()
        return reports

    def delete_drift_reports_by_model_id(self, model_id: str) -> Self:
        self.init_client()
        db = self.client[self.dbname]
        col = db[self.collection]
        try:
            col.delete_many({"model_id": model_id})
        except Exception as e:
            print(f"Error deleting drift reports by model id: {e}")
        finally:
            self.client.close()
        return self

    def delete_drift_reports_by_datetime_range(
        self, start: datetime, end: datetime
    ) -> Self:
        self.init_client()
        db = self.client[self.dbname]
        col = db[self.collection]
        try:
            col.delete_many({"timestamp": {"$gte": start, "$lte": end}})
        except Exception as e:
            print(f"Error deleting drift reports by datetime range: {e}")
        finally:
            self.client.close()
        return self

    def delete_drift_reports_by_model_id_and_datetime_range(
        self, model_id: str, start: datetime, end: datetime
    ) -> Self:
        self.init_client()
        db = self.client[self.dbname]
        col = db[self.collection]
        try:
            col.delete_many(
                {"model_id": model_id, "timestamp": {"$gte": start, "$lte": end}}
            )
        except Exception as e:
            print(f"Error deleting drift reports by model id and datetime range: {e}")
        finally:
            self.client.close()
        return self

    def delete_all_drift_reports(self) -> Self:
        self.init_client()
        db = self.client[self.dbname]
        col = db[self.collection]
        try:
            col.delete_many({})
        except Exception as e:
            print(f"Error deleting all drift reports: {e}")
        finally:
            self.client.close()
        return self

    def get_distinct_models(self) -> list[str]:
        self.init_client()
        db = self.client[self.dbname]
        col = db[self.collection]
        model_ids = []
        try:
            model_ids = [doc.model_id for doc in col.distinct("model_id")]
        except Exception as e:
            print(f"Error deleting all drift reports: {e}")
        finally:
            self.client.close()
        return model_ids
