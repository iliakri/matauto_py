import datetime
import importlib
import jsonpickle
import pytest
import json
from allure import step
from fixture.application import Application
from os.path import join, dirname, abspath
from fixture.dbase import DbFixture

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
    username = request.config.getoption("auth")
    cookies = None
    if username == "admin":
        api_config = load_config(request.config.getoption("--target") + ".json")['api']
        cookies = fixture.users.authorize(username=api_config['admin']['username'], password=api_config['admin']['password']).cookies
    elif username == "master":
        api_config = load_config(request.config.getoption("--target") + ".json")['api']
        cookies = fixture.users.authorize(username=api_config['master']['username'], password=api_config['master']['password']).cookies
    yield cookies


@pytest.fixture(scope="session")
def db(request):
    db_config = load_config(request.config.getoption("--target") + ".json")['db']
    dbfixture = DbFixture(host=db_config['host'], dbname=db_config['dbname'], user=db_config['user'], password=db_config['password'])
    yield dbfixture
    dbfixture.destroy()


def pytest_addoption(parser):
    parser.addoption("--target", action="store", default="chicken_dev", help="Choose stand: chicken_dev or prod")
    parser.addoption("--auth", action="store", default='admin', help="Choose auth: admin or master")


def pytest_itemcollected(item):
    """ we just collected a test item. """
    if item.config.getoption("--auth") == 'No':
        if 'cookies' in item.fixturenames:
            item.add_marker('xfail')
        else:
            item.add_marker('skip')

    '''if hasattr(item, 'callspec'):
        params = item.callspec.params
        print(params)
        if params:
            for key in params:
                param = str(params[key])
                param_len = len(param)'''
    # if item.get_marker('xfail'):


def pytest_generate_tests(metafunc):
    for fixture in metafunc.fixturenames:
        if fixture.startswith("data_"):
            testdata = load_from_module(fixture[5:])
            metafunc.parametrize(fixture, testdata)
        elif fixture.startswith("json_"):
            get_id_from_bd(fixture[5:])
            testdata = load_from_json(fixture[5:])
            metafunc.parametrize(fixture, testdata)


def load_from_module(module):
    return importlib.import_module("data.%s" % module).testdata


def load_from_json(file):
    with open(join(dirname(abspath(__file__)), "data/%s.json" % file)) as f:
        return jsonpickle.decode(f.read())


def load_from_bd(db):
    transporter_id = db.get_all_transporters_id()
    return transporter_id


@pytest.fixture
def x(request):
    return request.getfixturevalue(request.param)


def pytest_sessionstart(session):
    pass


def get_id_from_bd(objects):
    transporter_id = DbFixture(host='192.168.12.10', dbname='dev_production', user='vlad',
                               password='1').get_all_transporters_id(objects)
    file = join(dirname(abspath(__file__)), "data/%s.json" % objects)
    with open(file, "w") as out:
        jsonpickle.set_encoder_options("json", indent=2)
        out.write(jsonpickle.encode(transporter_id))


def pytest_make_parametrize_id(val, argname):
    if isinstance(val, int):
        return f'{argname}={val}'
    if isinstance(val, datetime.date):
        return f'{argname}'
    if isinstance(val, str):
        return f'{val}'
    return repr(val)


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
