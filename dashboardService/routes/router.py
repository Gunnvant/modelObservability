from __future__ import annotations
from fastapi import APIRouter
from fastapi.responses import HTMLResponse
from datetime import datetime
from services.db import db_service

router = APIRouter(prefix="/driftReport")


@router.get("/report/", response_class=HTMLResponse)
async def get_report(
    model_id: str):
    reports = db_service.get_drift_reports_by_model_id(model_id=model_id)
    r = reports[0]
    return r.report_html
