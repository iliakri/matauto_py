import requests
import pytest
from .support.assertions import assert_valid_schema


class TestClass:

    def test_get_hats(self, ppf_prod):
        res = ppf_prod.hats.get_hats()
        assert res.status_code == 200
        assert_valid_schema(res.json(), 'hats.json')
        assert len(res.json()) == 75

    def test_get_hats_by_workshop1(self, ppf_prod):
        res = ppf_prod.hats.get_hats_by_workshop(1)
        assert res.status_code == 200
        assert_valid_schema(res.json(), 'hats.json')

    def test_get_hats_by_workshop2(self, ppf_prod):
        res = ppf_prod.hats.get_hats_by_workshop(2)
        assert res.status_code == 200
        assert_valid_schema(res.json(), 'hats.json')

