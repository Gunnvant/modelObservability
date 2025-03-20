from __future__ import annotations
from pydantic import BaseModel
from datetime import datetime


class RequestReport(BaseModel):
    model_id: str
    date_range_start: datetime | None
    date_range_end: datetime | None
