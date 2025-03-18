import pytest
from mongoDBService.core import MongoDBService
from mongoDBService.entities import DriftReport
from datetime import datetime

def test_doc_insertion_deletion():
    service = MongoDBService(host='localhost', user=None, password=None, collection='test', dbname='test')
    report = DriftReport(
        model_id='123',
        report_html='html',
        timestamp=datetime(2025, 1, 1, 0, 0, 0))
    service.insert_drift_report(report)
    service.close_client()
    assert service.get_all_drift_reports() == [report]
    service.delete_all_drift_reports()
    assert service.get_all_drift_reports() == []

def test_get_reports_by_model_id():
    service = MongoDBService(host='localhost', user=None, password=None, collection='test', dbname='test')
    report = DriftReport(
        model_id='123',
        report_html='html',
        timestamp=datetime(2025, 1, 1, 0, 0, 0))
    service.insert_drift_report(report)
    service.close_client()
    assert service.get_drift_reports_by_model_id('123') == [report]
    service.delete_all_drift_reports()

def test_get_reports_by_date_range():
    service = MongoDBService(host='localhost', user=None, password=None, collection='test', dbname='test')
    report1 = DriftReport(
        model_id='123',
        report_html='html',
        timestamp=datetime(2025, 1, 1, 0, 0, 0))
    report2 = DriftReport(
        model_id='123',
        report_html='html',
        timestamp=datetime(2025, 1, 2, 0, 0, 0))
    service.insert_drift_report(report1)
    service.insert_drift_report(report2)
    reports = service.get_drift_reports_by_datetime_range(start=datetime(2025, 1, 1, 0, 0, 0),
                                                          end=datetime(2025, 1, 2, 0, 0, 0))
    assert reports == [report1, report2]
    service.delete_all_drift_reports()

def test_get_reports_by_model_id_and_date_range():
    service = MongoDBService(host='localhost', user=None, password=None, collection='test', dbname='test')
    report1 = DriftReport(
        model_id='123',
        report_html='html',
        timestamp=datetime(2025, 1, 1, 0, 0, 0))
    report2 = DriftReport(
        model_id='123',
        report_html='html',
        timestamp=datetime(2025, 1, 2, 0, 0, 0))
    service.insert_drift_report(report1)
    service.insert_drift_report(report2)
    reports = service.get_drift_reports_by_model_id_and_datetime_range(model_id='123',
                                                             start=datetime(2025, 1, 1, 0, 0, 0),
                                                             end=datetime(2025, 1, 2, 0, 0, 0))
    assert reports == [report1, report2]
    service.delete_all_drift_reports()

def test_delete_reports_by_model_id():
    service = MongoDBService(host='localhost', user=None, password=None, collection='test', dbname='test')
    report1 = DriftReport(
        model_id='123',
        report_html='html',
        timestamp=datetime(2025, 1, 1, 0, 0, 0))
    report2 = DriftReport(
        model_id='123',
        report_html='html',
        timestamp=datetime(2025, 1, 2, 0, 0, 0))
    service.insert_drift_report(report1)
    service.insert_drift_report(report2)
    service.delete_drift_reports_by_model_id('123')
    assert service.get_all_drift_reports() == []

def test_delete_reports_by_date_range():
    service = MongoDBService(host='localhost', user=None, password=None, collection='test', dbname='test')
    report1 = DriftReport(
        model_id='123',
        report_html='html',
        timestamp=datetime(2025, 1, 1, 0, 0, 0))
    report2 = DriftReport(
        model_id='123',
        report_html='html',
        timestamp=datetime(2025, 1, 2, 0, 0, 0))
    service.insert_drift_report(report1)
    service.insert_drift_report(report2)
    service.delete_drift_reports_by_datetime_range(start=datetime(2025, 1, 1, 0, 0, 0),
                                                   end=datetime(2025, 1, 2, 0, 0, 0))
    assert service.get_all_drift_reports() == []

def test_delete_reports_by_date_range_and_model_id():
    service = MongoDBService(host='localhost', user=None, password=None, collection='test', dbname='test')
    report1 = DriftReport(
        model_id='123',
        report_html='html',
        timestamp=datetime(2025, 1, 1, 0, 0, 0))
    report2 = DriftReport(
        model_id='123',
        report_html='html',
        timestamp=datetime(2025, 1, 2, 0, 0, 0))
    service.insert_drift_report(report1)
    service.insert_drift_report(report2)
    service.delete_drift_reports_by_model_id_and_datetime_range(model_id='123',
                                                                start=datetime(2025, 1, 1, 0, 0, 0),
                                                                end=datetime(2025, 1, 2, 0, 0, 0))
    assert service.get_all_drift_reports() == []

