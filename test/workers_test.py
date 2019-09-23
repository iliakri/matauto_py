import random
import json
import allure
import pytest
from data.worker import testdata


@pytest.mark.get
def test_get_worker_by_id(app, db):
    with allure.step("getting worker_id from db"):
        worker_id = random.choice(db.get_worker_by_id())
    with allure.step("get worker with worker_id=%s from api" % worker_id):
        res = app.workshops.get_worker_by_workshop(1, worker_id)
    print(json.dumps(res.json(), ensure_ascii=False, indent=2))
    assert res.status_code == 200
    assert res.headers['Content-Type'] == "application/json"
    app.schemas.assert_valid_schema(res.json(), 'worker_by_workshop.json')
    assert str(res.json().get("id")) == str(worker_id)


@pytest.mark.get
@pytest.mark.parametrize("workshop_id", (1, 2))
def test_get_workers_by_workshop(app, workshop_id):
    res = app.workshops.get_workers_by_workshop(workshop_id)
    assert res.status_code == 200
    assert res.headers['Content-Type'] == "application/json"
    app.schemas.assert_valid_schema(res.json(), 'workers_by_workshop.json')


@pytest.mark.get
def test_reports(app):
    res = app.workshops.get_workers_status_by_workshop(3, '2019-09-23')
    print(json.dumps(res.json(), ensure_ascii=False, indent=2))
    assert res.status_code == 200


@pytest.mark.parametrize("worker", testdata)
def test_create_worker(app, worker):
    res = app.workshops.create_worker_by_workshop(1, worker)
    print(json.dumps(res.json(), ensure_ascii=False, indent=2))
    assert res.status_code == 200
    assert res.headers['Content-Type'] == "application/json"
    app.schemas.assert_valid_schema(res.json(), 'worker_by_workshop.json')

