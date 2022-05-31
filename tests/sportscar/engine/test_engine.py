from multiprocessing.connection import wait
from pytest import mark

@mark.smoke
@mark.engine
def test_engine_functions_as_expeceted():
    assert True

@mark.ui
def test_get_engine_page(chrome_browser):
    chrome_browser.get("https://docs.pytest.org/en/6.2.x/example/index.html")
    assert True

