import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = None


# this name and arg are mandatory
def setup_module(module):
    global driver
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.implicitly_wait(10)
    driver.maximize_window()
    driver.delete_all_cookies()
    driver.get("https://www.google.com")


# this name and arg are mandatory
def teardown_module(module):
    driver.quit()


def test_google_title():
    assert driver.title == 'Google', "title didn't match"