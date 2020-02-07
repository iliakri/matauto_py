from allure import step, attach
import pytest
import os
import pandas as pd
import random
from io import BytesIO
from generator.worker import start_date, transporter_id


@pytest.mark.get
@pytest.mark.parametrize("workshop_id", [1, 2])
def test_get_transporters_by_workshop(api, cookies, workshop_id):
    res = api.workshops.get_transporters_by_workshop(workshop_id, cookies)
    api.assertion.status_code(res, [200])
    assert res.headers['Content-Type'] == "application/json"
    if res.json():
        api.schemas.assert_valid_schema(res.json(), 'transporters.json')


@pytest.mark.get
@pytest.mark.parametrize("transporter_id, start_date", start_date)
def test_get_shifts(api, transporter_id, start_date, cookies):
    res = api.transporters.get_shifts_by_transporter(transporter_id, start_date, cookies=cookies)
    api.assertion.status_code(res, [200])
    assert res.headers['Content-Type'] == "application/json"
    if res.json():
        api.schemas.assert_valid_schema(res.json(), 'shifts.json')


@pytest.mark.get
def test_get_shift(api, db, cookies):
    shift_id = random.choice(db.get_id_from_db('shift'))
    res = api.workshops.get_shift_by_id(shift_id, cookies)
    api.assertion.status_code(res, [200])
    assert res.headers['Content-Type'] == "application/json"
    if res.json():
        api.schemas.assert_valid_schema(res.json(), 'shift_by_id.json')


@pytest.mark.get
@pytest.mark.parametrize("transporter_id", transporter_id)
def test_get_cameras(api, transporter_id, cookies):
    res = api.transporters.get_cameras_by_transporter(transporter_id, cookies)
    api.assertion.status_code(res, [200])
    assert res.headers['Content-Type'] == "application/json"
    if res.json():
        api.schemas.assert_valid_schema(res.json(), 'cameras.json')


@pytest.mark.get
@pytest.mark.parametrize("transporter_id", transporter_id)
def test_get_productions(api, transporter_id, cookies):
    res = api.transporters.get_productions_by_transporter(transporter_id, cookies)
    api.assertion.status_code(res, [200])
    assert res.headers['Content-Type'] == "application/json"
    if res.json():
        api.schemas.assert_valid_schema(res.json(), 'productions.json')


@pytest.mark.get
@pytest.mark.parametrize("transporter_id, start_date", start_date)
def test_get_workers_status(api, transporter_id, start_date, cookies):
    res = api.transporters.get_workers_status_by_transporters(transporter_id, start_date, cookies=cookies)
    api.assertion.status_code(res, [200])
    assert res.headers['Content-Type'] == "application/json"
    if res.json():
        api.schemas.assert_valid_schema(res.json(), 'workers_status.json')


@pytest.mark.get
@pytest.mark.parametrize("transporter_id, start_date", start_date)
def test_get_reports(api, transporter_id, start_date, cookies):
    res = api.transporters.download_report_by_transporter(transporter_id, start_date, cookies=cookies)
    api.assertion.status_code(res, [200])
    filename = f'report_transporter_{transporter_id}_for_{start_date}'
    with step("Get report"):
        bio = BytesIO(res.content)
        writer = pd.ExcelWriter(bio)
        data_xls = pd.read_excel(writer, sheet_name='Отчёт', index_col=None)
        data_xls.to_csv(filename, encoding='utf-8', index=False, header=False)
    with step("Attach report"):
        attach.file(filename, name=filename, attachment_type="text/csv", extension=".csv")
        os.remove(filename)


@pytest.mark.post
@pytest.mark.parametrize("transporter_id", transporter_id)
def test_delete_production(api, db, cookies, transporter_id):
    with step("add production to transporter if none"):
        if len(db.get_production_id_by_transporter(transporter_id)) == 0:
            add_production = api.transporters.add_production_to_transporter(transporter_id, 1, cookies)
            api.assertion.status_code(add_production, [200])
    old_productions = db.get_production_id_by_transporter(transporter_id)
    production_id = random.choice(old_productions)
    res = api.transporters.del_production_from_transporter(transporter_id, production_id, cookies)
    api.assertion.status_code(res, [200])
    new_productions = db.get_production_id_by_transporter(transporter_id)
    assert len(old_productions) - 1 == len(new_productions)
