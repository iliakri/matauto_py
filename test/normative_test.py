import pytest
from generator.worker import transporter_id


@pytest.mark.get
@pytest.mark.parametrize("transporter_id", transporter_id)
def test_get_normative(api, transporter_id, cookies):
    res = api.transporters.get_normative_by_transporter(transporter_id, cookies)
    api.assertion.status_code(res, [200])
    if res.json():
        api.schemas.assert_valid_schema(res.json(), 'normatives.json')


@pytest.mark.post
@pytest.mark.parametrize("transporter_id", transporter_id)
def test_create_normative(api, transporter_id, cookies):
    res = api.transporters.create_normative(1, 2, 3, 4, cookies)
    api.assertion.status_code(res, [200])
    if res.json():
        assert str(res.json().get("result")) == "ok"

