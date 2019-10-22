import json


def test_sender_hats(app):
    res = app.sender.post_hats(workshop_id=1, zone_sub_id=15, hat_id=26, transporter_id=1)
    print(json.dumps(res.json(), ensure_ascii=False, indent=2))


def test_sender_productions(app):
    res = app.sender.post_productions(transporter_id=1, zone_sub_id=2, summ_out=3)
    print(json.dumps(res.json(), ensure_ascii=False, indent=2))