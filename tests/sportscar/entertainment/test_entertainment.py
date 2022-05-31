from pytest import mark

@mark.entertainment
def test_entertainment_function_as_expeceted():
    assert True

#@mark.ui
def test_can_get_entertainment_page(chrome_browser):
    chrome_browser.get("https://docs.pytest.org/en/6.2.x/customize.html")
    assert True
