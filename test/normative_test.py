def test_get_normative(app):
    res = app.workshops.get_normative(1)
    assert res.status_code == 200


def test_create_normative(app):
    res = app.workshops.create_normative(1, 2, 3, 4)
    assert res.status_code == 200
