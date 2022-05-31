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
# Fixture can use a fixture
def app_config(env):
    cfg = Config(env)
    return cfg



