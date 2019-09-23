import json
import pytest


@pytest.mark.get
@pytest.mark.parametrize("workshop_id", (1, 2))
def test_get_hats_by_workshop(app, workshop_id):
    res = app.workshops.get_hats_by_workshop(workshop_id)
    # print(json.dumps(res.json(), ensure_ascii=False, indent=2))
    assert res.status_code == 200
    assert res.headers['Content-Type'] == "application/json"
    app.schemas.assert_valid_schema(res.json(), 'hats.json')


