
def test_get_zones(app):
    res = app.zones.get_zones()
    assert res.status_code == 200
    app.schemas.assert_valid_schema(res.json(), 'zones.json')