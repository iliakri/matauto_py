import pytest


@pytest.mark.get
def test_get_workshops(api):
    res = api.workshops.get_workshops()
    api.assertion.status_code(res, [200])


@pytest.mark.get
def test_get_workshops_by_id(api):
    res = api.workshops.get_workshop_by_id(1)
    api.assertion.status_code(res, [200])
    assert res.headers['Content-Type'] == "application/json"
    if res.json():
        api.schemas.assert_valid_schema(res.json(), 'workshop.json')


@pytest.mark.get
def test_negative_get_workshops_by_id(api):
    res = api.workshops.get_workshop_by_id(10000)
    api.assertion.status_code(res, [200])