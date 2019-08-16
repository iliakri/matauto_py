
def test_get_workshops(app):
    res = app.hats.get_workshops()
    assert res.status_code == 200