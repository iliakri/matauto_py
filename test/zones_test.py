
def test_get_zones(app):
    res = app.zones.get_zones()
    assert res.status_code == 200
    assert res.headers['Content-Type'] == "application/json"
    app.schemas.assert_valid_schema(res.json(), 'zones.json')


def test_get_zones_for_conveyor(app):
    for conveyor_id in range(1, 5):
        res = app.zones.get_zones_for_conveyor(conveyor_id)
        assert res.status_code == 200
        assert res.headers['Content-Type'] == "application/json"
        app.schemas.assert_valid_schema(res.json(), 'zones.json')


