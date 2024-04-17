import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption("--browser")



@pytest.fixture
def browser(request):
    return request.config.getoption("--browser")


@pytest.fixture
def setup(browser):
    if browser == "Chrome":
        driver = webdriver.Chrome()
        print("Launching Chrome browser")

    elif browser == "Firefox":
      driver=webdriver.Firefox()
      print("Launching Firefox Browser")


    elif browser == "Edge":
        driver = webdriver.Edge()
        print("Launching Edge Browser")

    else:
        browser == "headless"
        chrome_options=webdriver.ChromeOptions()
        chrome_options.add_argument("headless")
        driver = webdriver.Chrome(options=chrome_options)

    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    return driver



@pytest.fixture(params=[
    ("John Doe","ThisIsNotAPassword","Pass"),
    ("John Doe12", "ThisIsNotAPassword", "Fail"),
    ("John Doe", "ThisIsNotAPassword123", "Fail"),
    ("John Doe123", "ThisIsNotAPassword124", "Fail")

])

def getdataforlogin(request):
    return request.param


def pytest_metadata(metadata):
    metadata["Environment"]= "Test"
    metadata["Project Name"] = "CureHealthcare"
    metadata["Module Name"] = "Employee"
    metadata["Tester"] = "Pruthviraj"
    # Remove
    metadata.pop("Packages",None)
    metadata.pop("Plugins",None)
    metadata.pop("Platform",None)




# @pytest.fixture
# def setup():
#     driver=webdriver.Chrome()
#     driver.get("https://katalon-demo-cura.herokuapp.com/")
#     driver.implicitly_wait(10)
#     driver.maximize_window()
#     yield driver
#     return driver
