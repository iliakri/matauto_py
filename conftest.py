import pytest
import json

from allure import step

from fixture.application import Application
from os.path import join, dirname, abspath
from fixture.db import DbFixture

fixture = None
target = None


def load_config(file):
    global target
    if target is None:
        config_file = join(dirname(abspath(__file__)), file)
        with open(config_file) as f:
            target = json.load(f)
    return target


@pytest.fixture(scope="session")
def api(request):
    global fixture
    api_config = load_config(request.config.getoption("--target") + ".json")['api']
    with step(f"Set API URL = {api_config['apiUrl']}"):
        fixture = Application(host=api_config['apiUrl'])
    return fixture


@pytest.fixture(scope="session")
def cookies(request):
    api_config = load_config(request.config.getoption("--target") + ".json")['api']
    cookies = fixture.users.authorize(username=api_config['username'], password=api_config['password']).cookies
    return cookies


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


"""def pytest_make_parametrize_id(val, argname):
    if isinstance(val, int):
        return f'{argname}={val}'
    if isinstance(val, datetime.date):
        return f'{argname}={val}'
    if isinstance(val, str):
        return f'text is {val}'
    return repr(val)"""


'''@pytest.fixture(scope="session", autouse="True")
def debug_requests_on():
    # Switches on logging of the requests module.
    HTTPConnection.debuglevel = 1
    logging.basicConfig()
    logging.getLogger().setLevel(logging.ERROR)
    requests_log = logging.getLogger("requests.packages.urllib3")
    requests_log.setLevel(logging.ERROR)
    requests_log.propagate = True'''


'''@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    setattr(item, "rep_" + report.when, report)
    if report.when == 'call' and report.failed:
        allure.attach(report.capstdout, 'out_log')'''

