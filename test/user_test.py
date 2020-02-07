from allure import step
import pytest
import random


@pytest.mark.get
def test_get_user_by_id(api, db, cookies):
    with step("Get a random user_id from DB"):
        user_id = random.choice(db.get_id_from_db('user'))
    with step(f"Get a random user with user_id = {user_id} from API"):
        res = api.users.get_user_by_id(user_id, cookies)
    api.assertion.status_code(res, [200])
    assert str(res.json().get("id")) == str(user_id)


@pytest.mark.get
def test_get_user_if_login(api):
    login = api.users.login('admin', 'admin')
    res = api.users.get_user_if_login(login.cookies)
    api.assertion.status_code(res, [200])


@pytest.mark.get
def test_get_all_users(api, cookies):
    res = api.users.get_all_users(cookies)
    api.assertion.status_code(res, [200])
    # todo assert schemas
    '''if res.json():
        app.schemas.assert_valid_schema(res.json(), 'all_users.json')'''


@pytest.mark.get
def test_logout(api, cookies):
    res = api.users.logout(cookies)
    api.assertion.status_code(res, [200])
    if res.json():
        assert str(res.json().get("status")) == "success"


@pytest.mark.get
def test_authorization(api):
    res = api.users.login(username='admin', password='admin')
    api.assertion.headers(res, 'Set-Cookie')
    api.assertion.status_code(res, [201])




'''def test_postman():
    url = "http://192.168.12.10:50020/api/v1/users/authorization"

    headers = {
    'Cookie': "session=.eJwlzrsRwzAIANBdqF1IIIHkZXx8xDmtHVe57J4ib4L3gSOvdZ-wv69nbXC8AnYopiWMXLpoXxRuGktQc0qfgimCNVosLd4ZiW2SjeCURpgjbJA55tSmLI21SzoqBmZhjpqqykZSbSBpoeSGGtVj9M4lhzfY4LnX9c9U-P4AAhov6w.XabzGg.mRGEYdPFzoiU9e6zXcW3hYUldcU"
    }

    response = requests.request("PUT", url, headers=headers)
    print(response.text)

    response = requests.request("GET", url, headers=headers)
    print(json.dumps(response.json(), ensure_ascii=False, indent=2))'''