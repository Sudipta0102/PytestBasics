import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = None


# function arg is optional here
def setup_function():
    global driver
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.implicitly_wait(10)
    driver.delete_all_cookies()
    driver.maximize_window()


def teardown_function(function):
    driver.quit()


def test_google():
    global driver
    driver.get("https://www.google.com")
    assert driver.title == 'Google', "title didn't match"


def test_insta():
    global driver
    driver.get("https://www.instagram.com")
    assert driver.title == 'Instagram', "title didn't match"
