import pytest


@pytest.mark.get
def test_get_user_by_id(app):
    user_id = 33
    res = app.users.get_user_by_id(user_id)
    app.assertion.status_code(res, [200])
    if res.json():
        assert str(res.json().get("id")) == str(user_id)


@pytest.mark.get
def test_get_user_if_login(app):
    res = app.users.get_user_if_login()
    app.assertion.status_code(res, [200])
    if res.json():
        assert str(res.json().get("id")) == "33"


@pytest.mark.get
def test_get_all_users(app):
    res = app.users.get_all_users()
    app.assertion.status_code(res, [200])
    '''if res.json():
        app.schemas.assert_valid_schema(res.json(), 'all_users.json')'''


@pytest.mark.get
def test_logout(app):
    res = app.users.logout()
    app.assertion.status_code(res, [200])
    if res.json():
        assert str(res.json().get("status")) == "success"


'''def test_postman():
    url = "http://192.168.12.10:50020/api/v1/users/authorization"

    headers = {
    'Cookie': "session=.eJwlzrsRwzAIANBdqF1IIIHkZXx8xDmtHVe57J4ib4L3gSOvdZ-wv69nbXC8AnYopiWMXLpoXxRuGktQc0qfgimCNVosLd4ZiW2SjeCURpgjbJA55tSmLI21SzoqBmZhjpqqykZSbSBpoeSGGtVj9M4lhzfY4LnX9c9U-P4AAhov6w.XabzGg.mRGEYdPFzoiU9e6zXcW3hYUldcU"
    }

    response = requests.request("PUT", url, headers=headers)
    print(response.text)

    response = requests.request("GET", url, headers=headers)
    print(json.dumps(response.json(), ensure_ascii=False, indent=2))'''