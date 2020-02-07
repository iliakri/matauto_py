from allure import step
import pytest
import random


@pytest.mark.get
def test_get_workshops(api, cookies):
    res = api.workshops.get_workshops(cookies)
    api.assertion.status_code(res, [200])


@pytest.mark.get
def test_get_workshops_by_id(api, db, cookies):
    with step("Get a random workshop_id from DB"):
        workshop_id = random.choice(db.get_id_from_db('workshop'))
    with step(f"Get a random workshop with workshop_id = {workshop_id} from API"):
        res = api.workshops.get_workshop_by_id(workshop_id, cookies)
    api.assertion.status_code(res, [200])
    assert str(res.json().get("id")) == str(workshop_id)


@pytest.mark.get
def test_negative_get_workshops_by_id(api, cookies):
    res = api.workshops.get_workshop_by_id(10000, cookies)
    api.assertion.status_code(res, [200])