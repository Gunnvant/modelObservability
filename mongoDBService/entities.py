from pydantic import BaseModel
from datetime import datetime


class MonitoringReport(BaseModel):
    model_id: str
    report_html: str
    report_json: str
    timestamp: datetime
