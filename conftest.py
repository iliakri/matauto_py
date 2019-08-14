import pytest

from fixture.application import Application


@pytest.fixture(scope="session")
def ppf_prod():
    ppf_prod = Application("http://10.8.1.11:50020/api/v1")
    return ppf_prod
