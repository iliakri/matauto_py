import random

import allure


def test_get_worker(app, db):
    with allure.step("getting worker_id from db"):
        worker_id = random.choice(db.get_worker_id()).id
    with allure.step("get worker with id=%s from api" % worker_id):
        res = app.workers.get_worker(worker_id)
    assert res.status_code == 200
    app.schemas.assert_valid_schema(res.json(), 'workers.json')
    assert res.json().get("id") == worker_id


def test_get_worker_by_workshop1(app):
    res = app.workers.get_worker_by_workshop(1)
    assert res.status_code == 200
    app.schemas.assert_valid_schema(res.json(), 'workers_by_workshop.json')


def test_get_worker_by_workshop2(app):
    res = app.workers.get_worker_by_workshop(2)
    assert res.status_code == 200
    app.schemas.assert_valid_schema(res.json(), 'workers_by_workshop.json')
