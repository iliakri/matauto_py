import random
import allure
import pytest
from generator.worker import data_for_create_worker


@pytest.mark.get
@pytest.mark.parametrize("workshop_id", [1, 2])
def test_get_worker_by_id(api, db, cookies, workshop_id):
    with allure.step("Get a random worker_id from DB"):
        worker_id = random.choice(db.get_workers_id_by_workshop(workshop_id))
    with allure.step(f"Get a random worker with worker_id = {worker_id} from API"):
        res = api.workshops.get_worker_by_workshop(workshop_id, worker_id, cookies)
    api.assertion.status_code(res, [200])
    if res.json():
        api.schemas.assert_valid_schema(res.json(), 'worker_by_workshop.json')
    assert str(res.json().get("id")) == str(worker_id)


@pytest.mark.get
@pytest.mark.parametrize("workshop_id", [1, 2])
def test_get_workers_by_workshop(api, cookies, workshop_id):
    res = api.workshops.get_workers_by_workshop(workshop_id, cookies)
    api.assertion.status_code(res, [200])
    if res.json():
        api.schemas.assert_valid_schema(res.json(), 'workers_by_workshop.json')


@pytest.mark.post
@pytest.mark.parametrize("worker", data_for_create_worker)
def test_create_worker(api, worker, cookies):
    res = api.workshops.create_worker_by_workshop(1, worker, cookies)
    api.assertion.status_code(res, [200])
    if res.json():
        api.schemas.assert_valid_schema(res.json(), 'worker_by_workshop.json')


@pytest.mark.get
@pytest.mark.parametrize("workshop_id", [1, 2])
def test_get_workers_with_paginated(api, cookies, workshop_id):
    res = api.workshops.get_workers_with_paginated(workshop_id, 1, 20, "asc", "name", "Ал", cookies)
    api.assertion.status_code(res, [200])
    # TODO different checks


@pytest.mark.get
def test_negative_get_workers_by_workshop(api, cookies):
    res = api.workshops.get_workers_by_workshop(6666, cookies)
    api.assertion.status_code(res, [400])
    if res.json():
        assert str(res.json().get("message")) == "Цех не найден"
