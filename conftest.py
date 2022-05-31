from time import sleep
from pytest import fixture
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# @fixture(scope='function')
@fixture(scope='session')
def chrome_browser():
    browser = webdriver.Chrome(ChromeDriverManager().install())
    # browser.implicitly_wait(0.5)
    #return browser

    yield browser
    sleep(5)
    #Teardown
    print("I am tearing down this browser!")