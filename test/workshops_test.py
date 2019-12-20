import pytest


@pytest.mark.get
def test_get_workshops(app):
    res = app.workshops.get_workshops()
    app.assertion.status_code(res, [200])


@pytest.mark.get
def test_get_workshops_by_id(app):
    res = app.workshops.get_workshop_by_id(1)
    app.assertion.status_code(res, [200])
    assert res.headers['Content-Type'] == "application/json"
    if res.json():
        app.schemas.assert_valid_schema(res.json(), 'workshop.json')


@pytest.mark.get
def test_negative_get_workshops_by_id(app):
    res = app.workshops.get_workshop_by_id(10000)
    app.assertion.status_code(res, [200])