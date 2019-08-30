
def test_get_zones(app):
    for transporter_id in range(1, 5):
        res = app.workshops.get_zones_by_transporter(transporter_id)
        assert res.status_code == 200
        assert res.headers['Content-Type'] == "application/json"
        app.schemas.assert_valid_schema(res.json(), 'zones.json')


def test_get_zones_status(app):
    for transporter_id in range(1, 5):
        res = app.workshops.get_status_of_zones_by_transporter(transporter_id)
        assert res.status_code == 200
        assert res.headers['Content-Type'] == "application/json"
        app.schemas.assert_valid_schema(res.json(), 'zones.json')


