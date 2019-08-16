import pytest
import json
from fixture.application import Application
from os.path import join, dirname, abspath
from fixture.db import DbFixture

target = None


def load_config(file):
    global target
    if target is None:
        config_file = join(dirname(abspath(__file__)), file)
        with open(config_file) as f:
            target = json.load(f)
    return target


@pytest.fixture(scope="session")
def app(request):
    global target
    api_config = load_config(request.config.getoption("--target") + ".json")['api']
    fixture = Application(host=api_config['apiUrl'])
    return fixture


@pytest.fixture(scope="session")
def db(request):
    db_config = load_config(request.config.getoption("--target") + ".json")['db']
    dbfixture = DbFixture(host=db_config['host'], dbname=db_config['dbname'], user=db_config['user'], password=db_config['password'])

    def fin():
        dbfixture.destroy()
    request.addfinalizer(fin)
    return dbfixture


def pytest_addoption(parser):
    parser.addoption("--target", action="store", default="chicken_dev")
