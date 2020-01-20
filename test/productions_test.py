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


@pytest.mark.post
def test_delete_production(api, db, cookies):
    transporter_id = 4
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



'''    list_production = api.transporters.get_productions_by_transporter(6).json()
    list_production_id = []
    for i in range(len(list_production)):
        list_production_id.append(list_production[i]['id'])'''