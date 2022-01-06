import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


# run this test with this command -> pytest -n 4 test_name.py -v
def test_google():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.implicitly_wait(10)
    driver.get("https://www.google.com")
    assert driver.title == 'Google', "title didn't match"
    driver.quit()


def test_insta():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.implicitly_wait(10)
    driver.get("https://www.instagram.com")
    assert driver.title == 'Instagram', "title didn't match"
    driver.quit()


def test_gmail():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.implicitly_wait(10)
    driver.get("https://www.gmail.com")
    assert driver.title == 'Gmail', "title didn't match"
    driver.quit()


def test_rediff():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.implicitly_wait(10)
    driver.get("https://www.rediff.com")
    assert driver.title == 'Rediff.com: News | Rediffmail | Stock Quotes | Shopping', "title didn't match"
    driver.quit()



