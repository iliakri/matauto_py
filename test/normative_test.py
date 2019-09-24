import pytest


@pytest.mark.get
@pytest.mark.parametrize("transporter_id", (1, 2, 3, 4))
def test_get_normative(app, transporter_id):
    res = app.workshops.get_normative(transporter_id)
    assert res.status_code == 200
    assert res.headers['Content-Type'] == "application/json"
    app.schemas.assert_valid_schema(res.json(), 'normatives.json')


@pytest.mark.parametrize("transporter_id", (1, 2, 3, 4))
def test_create_normative(app):
    res = app.workshops.create_normative(1, 2, 3, 4)
    assert res.status_code == 200
