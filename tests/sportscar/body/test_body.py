from pytest import mark

@mark.smoke
@mark.body
class Body: 
    def test_body_function_as_expeceted(self):
        assert True

    #@mark.ui
    def test_can_get_body_page(self,chrome_browser):
        chrome_browser.get("https://docs.pytest.org/en/6.2.x/contents.html")
        assert True


