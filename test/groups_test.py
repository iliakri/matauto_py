import pytest


@pytest.mark.get
def test_get_all_groups(api, cookies):
    res = api.groups.get_all_groups(cookies)
    api.assertion.status_code(res, [200])
    '''if res.json():
            app.schemas.assert_valid_schema(res.json(), 'all_groups.json')'''


@pytest.mark.get
def test_get_group(api, cookies):
    res = api.groups.get_group_by_id(1, cookies)
    api.assertion.status_code(res, [200])

