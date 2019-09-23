import pytest


@pytest.mark.get
@pytest.mark.parametrize("transporter_id", (1, 2, 3, 4))
def test_get_shifts(app, transporter_id):
    res = app.workshops.get_shift_by_transporter(transporter_id)
    assert res.status_code == 200
    assert res.headers['Content-Type'] == "application/json"
    app.schemas.assert_valid_schema(res.json(), 'shifts.json')


@pytest.mark.get
@pytest.mark.parametrize("shift_id", 110)
def test_get_shifts(app, shift_id):
    res = app.workshops.get_shift_by_id(shift_id)
    assert res.status_code == 200
    assert res.headers['Content-Type'] == "application/json"
    app.schemas.assert_valid_schema(res.json(), 'shift_by_id.json')