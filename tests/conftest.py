from pytest import fixture
from config import Config

#what info would be nice to pass in my test suite
def pytest_addoption(parser):
    parser.addoption(
                    "--env", 
                    action="store",
                    # default="",
                    help="Enviroment to run tests against. Configured in contest.py."
                    )

@fixture(scope='session')
#request available from pytest
# request holds all passed args to pytest
def env(request):
    return request.config.getoption("--env")


@fixture(scope='session')
# Fixture can use another fixture. In this case env.
# Env is whatever we pass arg we pass after --env
def app_config(env):
    cfg = Config(env) #want to build a config object with env fixture
    return cfg



