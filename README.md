## Notes

```
pytest -v
pytest -m engine

pytest -s #-s show standard out

```

Test Searching and Test Tagging

```
from pytest import mark

@mark.smoke
@mark.engine

```

Fixtures:

Any fixture created in conftest becomes available in that direcotry and any below it.

```
@fixture(scope=function) #e.e. One browser object per function
@fixture(scope=session) #i.e One browser for all tests
```

```
conftest.py

from pytest import fixture
from selenium import webdriver

@fixture(scope='function')
def chrome_browser():
    browser = webdriver.Chrome()
    #return browser

    yield browser

    #Teardown
    print("I am tearing down this browser!")

```

Reporting

```
pip install pytest-html

pytest --html="results.html"

#load xml into Jenkins
pytest --junitxml="results.xml"

```

Customizing Config

config.py

```
class Config:
    def __init__(self,env):

        SUPPORTED_ENVS = ['dev','qa']

        if env.lower() not in SUPPORTED_ENVS:
            raise Exception(f'{env} is not a supported enviroment. Supported envs: {SUPPORTED_ENVS}')

        self.base_url = {
            'dev':'https://mydev-env.com',
            'qa':'https://myqa-env.com'
        }[env]

        self.app_port = {
            'dev': 8080,
            'qa':80
        }[env]
```

conftest.py

```
from pytest import fixture

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
```

Python argparse
https://docs.python.org/3/library/argparse.html

```
pytest -h
# custom options:
# --env=ENV Enviroment to run tests against. Configured in contest.py.
```

Test that able to pass args to --env
pytest --env=qa -v

test_enviroment.py

```
#env is a fixture
def test_enviroment_is_qa(env):
    assert env == 'qa'

def test_enviroment_is_dev(env):
    assert env == 'dev'
```

Decorators

First class functions allow us to treat functions as objects.
Pass functions as arguments, return function and assign functions to variables.
A decorator is a function which takes another function as an argumnet.

```
def decorator_function(original_function):
    def wrapper_function():
        return original_function()
    return wrapper_function

# Modify original function by editing the wrapper.
# That way do not have to alter original functio.
```
