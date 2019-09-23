import pytest


@pytest.mark.get
def test_get_workshops(app):
    res = app.workshops.get_workshops()
    assert res.status_code == 200


@pytest.mark.get
@pytest.mark.parametrize("workshop_id", (1, 2))
def test_get_workshops_by_id(app, workshop_id):
    res = app.workshops.get_workshop_by_id(workshop_id)
    assert res.status_code == 200
    app.schemas.assert_valid_schema(res.json(), 'workshop.json')


@pytest.mark.get
def test_negative_get_workshops_by_id(app):
    res = app.workshops.get_workshop_by_id(10000)
    assert res.status_code == 400
    assert str(res.json().get("message")) == "Цех не найден."
