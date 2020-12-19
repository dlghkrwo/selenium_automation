from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import pytest

class TestAmazon:
    driver = ''

    def setup_method(self):
        self.driver = webdriver.Chrome()
        url = "https://www.youtube.com"
        self.driver.get(url)
        self.driver.maximize_window()
        time.sleep(2)

    def test_trending(self):
        self.driver.find_element(By.XPATH, 'guide-icon style-scope ytd-mini-guide-entry-renderer').click()

        elements = self.driver.find_element(By.CLASS_NAME, 'style-scope ytd-section-list-renderer')
        assert len(elements) > 1


