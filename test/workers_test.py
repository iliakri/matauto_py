import random
import allure
import pytest
from data.worker import data_for_create_worker


@pytest.mark.get
def test_get_worker_by_id(api, db):
    with allure.step("Get a random worker_id from DB"):
        worker_id = random.choice(db.get_worker_id())
    with allure.step(f"Get a random worker with worker_id = {worker_id} from API"):
        res = api.workshops.get_worker_by_workshop(1, worker_id)
    api.assertion.status_code(res, [200])
    if res.json():
        api.schemas.assert_valid_schema(res.json(), 'worker_by_workshop.json')
    assert str(res.json().get("id")) == str(worker_id)


@pytest.mark.get
def test_get_workers_by_workshop(api):
    res = api.workshops.get_workers_by_workshop(1)
    api.assertion.status_code(res, [200])
    if res.json():
        api.schemas.assert_valid_schema(res.json(), 'workers_by_workshop.json')


@pytest.mark.post
@pytest.mark.parametrize("worker", data_for_create_worker)
def test_create_worker(api, worker):
    res = api.workshops.create_worker_by_workshop(1, worker)
    api.assertion.status_code(res, [200])
    if res.json():
        api.schemas.assert_valid_schema(res.json(), 'worker_by_workshop.json')


@pytest.mark.get
def test_get_workers_with_paginated(api):
    res = api.workshops.get_workers_with_paginated(1, 1, 10, "name", "ASC", "Ал")
    api.assertion.status_code(res, [200])


@pytest.mark.get
def test_negative_get_workers_by_workshop(api):
    res = api.workshops.get_workers_by_workshop(1000)
    api.assertion.status_code(res, [200])
    if res.json():
        assert str(res.json().get("message")) == "Цех не найден"
