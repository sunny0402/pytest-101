from pytest import fixture
# For browser automation
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
#edge
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager
# For data driven tests.
import json

data_path = 'test_data.json'

# TODO: debug webdriver_manager
# Any test which calls this fixture. Will run the test one time for any parameter in here.
# @fixture(params=[
#     webdriver.Chrome(ChromeDriverManager().install()),
#     webdriver.Firefox(service=Service(GeckoDriverManager().install())),
#     webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))
# ])
# def browser(request):
#     driver = request.param #each of params list items
#     #drvr = driver()
#     yield driver
#     driver.quit()


# Run test for every item in JSON file.
def load_test_data(path):
    with open(path) as data_file:
        data = json.load(data_file)
        return data

# Define a fixture to parametrize the test data and pass to tests.
@fixture(params=load_test_data(data_path))
def test_data(request):
    data = request.param #data will be each list item in test_data.json
    return data