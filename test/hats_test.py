import json
import pytest


@pytest.mark.get
def test_get_hats_by_workshop(app):
    res = app.workshops.get_hats_by_workshop(1)
    # print(json.dumps(res.json(), ensure_ascii=False, indent=2))
    assert res.status_code == 200
    assert res.headers['Content-Type'] == "application/json"
    app.schemas.assert_valid_schema(res.json(), 'hats.json')


def test_download_hats_by_workshop(app):
    res = app.workshops.download_hats_by_workshop(1)
    assert res.status_code == 200


@pytest.mark.get
def test_negative_get_hats_by_workshop(app):
    res = app.workshops.get_hats_by_workshop(1000)
    assert res.status_code == 404

