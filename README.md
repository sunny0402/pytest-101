## Notes

Review other branches for test enviroment configuration. And test parametrization for data driven test set up.

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
