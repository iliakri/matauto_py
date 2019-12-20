import pytest


@pytest.mark.get
@pytest.mark.parametrize("transporter_id", (1, 2, 3, 4))
def test_get_zones(app, transporter_id):
    res = app.workshops.get_zones_by_transporter(transporter_id)
    app.assertion.status_code(res, [200])
    if res.json():
        app.schemas.assert_valid_schema(res.json(), 'zones.json')


@pytest.mark.get
@pytest.mark.parametrize("transporter_id", (1, 2, 3, 4))
def test_get_zones_status(app, transporter_id):
    res = app.workshops.get_status_of_zones_by_transporter(transporter_id)
    app.assertion.status_code(res, [200])
    if res.json():
        app.schemas.assert_valid_schema(res.json(), 'zones.json')
