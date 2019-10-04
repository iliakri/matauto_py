import json
import pytest


@pytest.mark.get
def test_login_required(app):
    res = app.session.login_required()
    print(json.dumps(res.json(), ensure_ascii=False, indent=2))
    assert res.status_code == 200


@pytest.mark.get
def test_get_user(app):
    res = app.session.get_user_if_login()
    print(json.dumps(res.json(), ensure_ascii=False, indent=2))
    assert res.status_code == 200


@pytest.mark.get
def test_logout(app):
    res = app.session.logout()
    print(json.dumps(res.json(), ensure_ascii=False, indent=2))
    assert res.status_code == 200
