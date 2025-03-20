from evidently.report import Report
from evidently.metric_preset import DataDriftPreset
from datetime import datetime
from mongoDBService.entities import DriftReport
import pandas as pd
from abc import ABC, abstractmethod


class MonitoringInterface(ABC):
    @abstractmethod
    def get_report(self):
        pass


class DataDriftService(MonitoringInterface):
    def __init__(
        self, model_id: str, reference_data: pd.DataFrame, current_data: pd.DataFrame
    ):
        self.model_id = model_id
        self.reference_data = reference_data
        self.current_data = current_data

    def get_report(self) -> DriftReport:
        report_html = self._get_data_drift_report()
        result = DriftReport(
            model_id=self.model_id, report_html=report_html, timestamp=datetime.now()
        )
        return result

    def _get_data_drift_report(self):
        report = Report(metrics=[DataDriftPreset()])
        report.run(reference_data=self.reference_data, current_data=self.current_data)
        return report.get_html()


class DataQualityService(MonitoringInterface):
    pass


class ModelMonitoringService(MonitoringInterface):
    pass
