from allure import step
import pytest
import random


@pytest.mark.get
def test_get_all_groups(api, cookies):
    res = api.groups.get_all_groups(cookies)
    api.assertion.status_code(res, [200])
    # todo assert shemas
    '''if res.json():
            api.schemas.assert_valid_schema(res.json(), 'all_groups.json')'''


@pytest.mark.get
def test_get_group(api, db, cookies):
    with step("Get a random group_id from DB"):
        group_id = random.choice(db.get_id_from_db('group'))
    with step(f"Get a random group with group_id = {group_id} from API"):
        res = api.groups.get_group_by_id(group_id, cookies)
    api.assertion.status_code(res, [200])
    assert str(res.json().get("id")) == str(group_id)

