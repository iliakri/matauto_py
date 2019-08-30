import random

import allure


def test_get_worker_by_id(app, db):
    with allure.step("getting worker_id from db"):
        worker_id = random.choice(db.get_worker_by_id())
    with allure.step("get worker with worker_id=%s from api" % worker_id):
        res = app.workshops.get_worker_by_workshop(1, worker_id)
    assert res.status_code == 200
    assert res.headers['Content-Type'] == "application/json"
    app.schemas.assert_valid_schema(res.json(), 'worker_by_workshop.json')
    assert str(res.json().get("id")) == str(worker_id)


def test_get_workers_by_workshop1(app):
    res = app.workshops.get_workers_by_workshop(1)
    assert res.status_code == 200
    assert res.headers['Content-Type'] == "application/json"
    app.schemas.assert_valid_schema(res.json(), 'workers_by_workshop.json')

