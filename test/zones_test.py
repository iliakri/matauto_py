import pytest


@pytest.mark.get
@pytest.mark.parametrize("transporter_id", (1, 2, 3, 4))
def test_get_zones(api, transporter_id):
    res = api.transporters.get_zones_by_transporter(transporter_id)
    api.assertion.status_code(res, [200])
    if res.json():
        api.schemas.assert_valid_schema(res.json(), 'zones.json')


@pytest.mark.get
@pytest.mark.parametrize("transporter_id", (1, 2, 3, 4))
def test_get_zones_status(api, transporter_id):
    res = api.transporters.get_zones_status_by_transporter(transporter_id)
    api.assertion.status_code(res, [200])
    if res.json():
        api.schemas.assert_valid_schema(res.json(), 'zones.json')
