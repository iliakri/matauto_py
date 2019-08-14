import pytest
import json

from fixture.application import Application
from os.path import join, dirname, abspath

target = None


@pytest.fixture(scope="session")
def app(request):
    global target
    if target is None:
        config_file = join(dirname(abspath(__file__)), request.config.getoption("--target"))
        with open(config_file) as f:
            target = json.load(f)

    fixture = Application(host=target['apiUrl'])
    return fixture


def pytest_addoption(parser):
    parser.addoption("--target", action="store", default="ppf_prod.json")
