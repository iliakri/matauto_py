from allure import step
import pytest
import random


@pytest.mark.get
def test_get_all_productions(api, cookies):
    res = api.productions.get_all_productions(cookies)
    api.assertion.status_code(res, [200])
    '''if res.json():
            app.schemas.assert_valid_schema(res.json(), 'all_productions.json')'''


@pytest.mark.get
def test_get_production_by_id(api, db, cookies):
    with step("Get a random production_id from DB"):
        production_id = random.choice(db.get_productions_id())
    with step(f"Get a random production with production_id = {production_id} from API"):
        res = api.productions.get_production_by_id(production_id, cookies)
    api.assertion.status_code(res, [200])
    assert str(res.json().get("id")) == str(production_id)