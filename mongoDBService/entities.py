from pydantic import BaseModel
from datetime import datetime


class DriftReport(BaseModel):
    model_id: str
    report_html: str
    timestamp: datetime
