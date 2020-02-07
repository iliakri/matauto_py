import pytest


@pytest.mark.post
def test_sender_hats(api, cookies):
    res = api.sender.post_hats(workshop_id=1, zone_sub_id=5, hat_id=20, transporter_id=1)
    api.assertion.status_code(res, [200])


@pytest.mark.post
def test_sender_productions(api, cookies):
    res = api.sender.post_productions(transporter_id=1, zone_sub_id=2, summ_out=3)
    api.assertion.status_code(res, [200])