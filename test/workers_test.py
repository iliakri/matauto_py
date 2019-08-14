from random import randint


def test_get_worker(app):
    uid = randint(26, 66)
    print("uid=" + str(uid))
    res = app.workers.get_worker(uid)
    assert res.status_code == 200
    app.schemas.assert_valid_schema(res.json(), 'workers.json')
    assert res.json().get("id") == uid


def test_get_worker_by_workshop1(app):
    res = app.workers.get_worker_by_workshop(1)
    assert res.status_code == 200
    app.schemas.assert_valid_schema(res.json(), 'workers_by_workshop.json')


def test_get_worker_by_workshop2(app):
    res = app.workers.get_worker_by_workshop(2)
    assert res.status_code == 200
    app.schemas.assert_valid_schema(res.json(), 'workers_by_workshop.json')
