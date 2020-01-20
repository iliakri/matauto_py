import os
import pandas as pd
from io import BytesIO
import allure
import pytest


@pytest.mark.get
def test_get_hats_by_workshop(api, cookies):
    res = api.workshops.get_hats_by_workshop(1, cookies)
    api.assertion.status_code(res, [200])
    if res.json():
        api.schemas.assert_valid_schema(res.json(), 'hats.json')


@pytest.mark.get
def test_download_hats_by_workshop(api, cookies):
    res = api.workshops.download_hats_by_workshop(1, cookies)
    api.assertion.status_code(res, [200])
    filename = f'hats_list'
    with allure.step("Get report"):
        bio = BytesIO(res.content)
        writer = pd.ExcelWriter(bio)
        data_xls = pd.read_excel(writer, sheet_name='Список', index_col=None)
        data_xls.to_csv(filename, encoding='utf-8', index=False, header=False)
    with allure.step("Attach report"):
        allure.attach.file(filename, name=filename, attachment_type="text/csv", extension=".csv")
        os.remove(filename)


@pytest.mark.get
def test_negative_get_hats_by_workshop(api, cookies):
    res = api.workshops.get_hats_by_workshop(1000, cookies)
    api.assertion.status_code(res, [200])

