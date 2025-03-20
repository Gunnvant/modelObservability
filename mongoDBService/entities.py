from pydantic import BaseModel
from datetime import datetime


class DriftReportHtml(BaseModel):
    model_id: str
    report_html: str
    timestamp: datetime
