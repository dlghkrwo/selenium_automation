from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import time
import pytest

class TestAmazon:
    driver = ''

    def setup_method(self):
        self.driver = webdriver.Chrome()
        url = "https://www.amazon.com"
        self.driver.get(url)
        self.driver.maximize_window()
        time.sleep(2)
        self.driver.get('https://www.amazon.com/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3Fref_%3Dnav_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&')
        login = self.driver.find_element(By.ID, 'ap_email')
        login.send_keys('ghkrzkdlf@gmail.com', Keys.ENTER)
        password = self.driver.find_element(By.ID, 'ap_password')
        password.send_keys('ghkrzkdlf1', Keys.ENTER)
        time.sleep(2)


    def test_amazon_search(self):
        search = self.driver.find_element(By.ID, 'twotabsearchtextbox')
        search.send_keys('iphone 12', Keys.ENTER)
        # img = self.driver.find_element(By.XPATH, "img[@class='sb_s0WWAh6z']")
        self.driver.find_element(By.XPATH, "//input[@class='a-button-input' and @aria-labelledby='a-autoid-29-announce']")

        expected_text = '"iphone 12"'
        actual_text = self.driver.find_element(By.XPATH, "//span[@class='a-color-state a-text-bold']").text
        assert expected_text == actual_text, f'Error, Expected text :{expected_text}, but actual text:{actual_text}'

   
