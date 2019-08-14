
class TestClass:

    def test_get_hats(self, app):
        res = app.hats.get_hats()
        assert res.status_code == 200
        app.schemas.assert_valid_schema(res.json(), 'hats.json')
        assert len(res.json()) == 75

    def test_get_hats_by_workshop1(self, app):
        res = app.hats.get_hats_by_workshop(1)
        assert res.status_code == 200
        app.schemas.assert_valid_schema(res.json(), 'hats.json')

    def test_get_hats_by_workshop2(self, app):
        res = app.hats.get_hats_by_workshop(2)
        assert res.status_code == 200
        app.schemas.assert_valid_schema(res.json(), 'hats.json')
