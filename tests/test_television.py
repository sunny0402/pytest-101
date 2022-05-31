from pytest import mark


# Parametrize tv_brand variable
# Inject iterables
# Problem here is that data is associate with test case.
@mark.skip
@mark.parametrize('tv_brand', [
    ('Samsung'),
    ('Sony'),
    ('Visio')
])
def test_television_turns_on(tv_brand):
    print(f"{tv_brand} turns on as expected.")


# Test that feautre is supported by multple browsers.
@mark.skip
def test_browser_can_navigate_to_cffi(browser):
    browser.get('https://cffi.readthedocs.io/en/latest/')


# Data driven testing.
# test_data is a fixture defined in conftest.py
# so the test is parametrize at fixture level.
def test_product_with_input_data(test_data):
    print(f"{test_data} turns on as expected.")


