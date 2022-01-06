import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.chrome.service import Service

driver = None


@pytest.fixture(scope='module')
def init_driver():
    global driver
    print("_"*30 + "setup" + "_"*30)
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.implicitly_wait(10)
    driver.maximize_window()
    driver.delete_all_cookies()
    driver.get("https://www.google.com")
    yield
    print("_" * 30 + "teardown" + "_" * 30)
    driver.quit()


# 1. this is one way, which is using this as an argument
def test_google_title(init_driver):
    assert driver.title == 'Google', "title didn't match"


# 2. this is another way, better way.
@pytest.mark.usefixtures('init_driver')
def test_google_title1():
    assert driver.title == 'Google', "title didn't match"
