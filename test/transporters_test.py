import allure
import pytest
import json
import os

from data.worker import start_date


@pytest.mark.get
def test_get_transporters_by_workshop(app):
    res = app.workshops.get_transporters_by_workshop(1)
    assert res.status_code == 200
    assert res.headers['Content-Type'] == "application/json"
    app.schemas.assert_valid_schema(res.json(), 'transporters.json')


@pytest.mark.get
@pytest.mark.parametrize("transporter_id", (1, 2, 3, 4))
def test_get_shifts(app, transporter_id):
    res = app.workshops.get_shift_by_transporter(transporter_id, '2019-09-24')
    print(json.dumps(res.json(), ensure_ascii=False, indent=2))
    assert res.status_code == 200
    assert res.headers['Content-Type'] == "application/json"
    app.schemas.assert_valid_schema(res.json(), 'shifts.json')


@pytest.mark.get
@pytest.mark.parametrize("shift_id", (110, 109))
def test_get_shift(app, shift_id):
    res = app.workshops.get_shift_by_id(shift_id)
    assert res.status_code == 200
    assert res.headers['Content-Type'] == "application/json"
    app.schemas.assert_valid_schema(res.json(), 'shift_by_id.json')


@pytest.mark.get
@pytest.mark.parametrize("transporter_id", (1, 2, 3, 4))
def test_get_cameras(app, transporter_id):
    res = app.workshops.get_cameras_by_transporter(transporter_id)
    assert res.status_code == 200
    assert res.headers['Content-Type'] == "application/json"
    app.schemas.assert_valid_schema(res.json(), 'cameras.json')


@pytest.mark.get
@pytest.mark.parametrize("transporter_id", (1, 2, 3, 4))
def test_get_productions(app, transporter_id):
    res = app.workshops.get_productions_by_transporter(transporter_id)
    assert res.status_code == 200
    assert res.headers['Content-Type'] == "application/json"
    app.schemas.assert_valid_schema(res.json(), 'productions.json')


@pytest.mark.get
@pytest.mark.parametrize("transporter_id", (1, 2, 3, 4))
def test_get_workers_status(app, transporter_id):
    res = app.workshops.get_workers_status_by_transporters(transporter_id, '2019-09-23')
    assert res.status_code == 200
    assert res.headers['Content-Type'] == "application/json"
    app.schemas.assert_valid_schema(res.json(), 'workers_status.json')


@pytest.mark.get
@pytest.mark.parametrize("transporter_id, start_date", start_date)
def test_get_reports(app, transporter_id, start_date):
    res = app.workshops.download_report_by_transporter(transporter_id, start_date)
    assert res.status_code == 200
    filename = f'report_transporter{transporter_id}_for_{start_date}.xlsx'
    output = open(filename, 'wb')
    output.write(res.content)
    output.close()
    allure.attach(res.content, filename, "text/csv", ".xlsx")
    os.remove(filename)



