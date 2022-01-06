# didn't work

import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


class TestAll:
    driver = None

    def setup_method(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.implicitly_wait(10)
        self.driver.delete_all_cookies()
        self.driver.maximize_window()

    def teardown_method(self):
        self.driver.quit()

    def test_google(self):
        self.driver.get("https://www.google.com")
        assert self.driver.title == 'Google', "title didn't match"

    def test_insta(self):
        self.driver.get("https://www.instagram.com")
        assert self.driver.title == 'Instagram', "title didn't match"


obj = TestAll()
obj.test_google()
obj.test_insta()