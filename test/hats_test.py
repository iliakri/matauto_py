def test_get_hats_by_workshop1(app):
    res = app.workshops.get_hats_by_workshop(1)
    assert res.status_code == 200
    assert res.headers['Content-Type'] == "application/json"
    app.schemas.assert_valid_schema(res.json(), 'hats.json')

