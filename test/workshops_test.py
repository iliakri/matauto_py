
def test_get_workshops(app):
    res = app.workshops.get_workshops()
    assert res.status_code == 200


def test_get_workshops_by_id1(app):
    res = app.workshops.get_workshop_by_id(1)
    assert res.status_code == 200

