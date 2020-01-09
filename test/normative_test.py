import pytest


@pytest.mark.get
@pytest.mark.parametrize("transporter_id", (1, 2, 3, 4))
def test_get_normative(app, transporter_id):
    res = app.transporters.get_normative_by_transporter(transporter_id)
    app.assertion.status_code(res, [200])
    if res.json():
        app.schemas.assert_valid_schema(res.json(), 'normatives.json')


@pytest.mark.post
@pytest.mark.parametrize("transporter_id", (1, 2, 3, 4))
def test_create_normative(app, transporter_id):
    res = app.transporters.create_normative(1, 2, 3, 4)
    app.assertion.status_code(res, [200])
    if res.json():
        assert str(res.json().get("result")) == "ok"

