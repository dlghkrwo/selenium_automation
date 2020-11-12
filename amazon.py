from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import pyautogui
import time

driver = webdriver.Chrome()
url = "https://amazon.com"
driver.get(url)
driver.maximize_window()
action = ActionChains(driver)
#elem = driver.find_element_by_name('q')
#elem.send_keys('calculus')

driver.get('https://www.amazon.com/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3Fref_%3Dnav_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&')

time.sleep(2)

action.send_keys('ghkrzkdlf@gmail.com').perform()
#action.reset_actions()

time.sleep(2)

action = ActionChains(driver)

driver.find_element_by_id('continue').click()
time.sleep(2)
action.send_keys('ghkrzkdlf1').perform()
action.reset_actions()
time.sleep(2)

action = ActionChains(driver)
driver.find_element_by_id('auth-signin-button').click()
time.sleep(3)

driver.find_element_by_css_selector('.nav-search-field').click()
time.sleep(2)

action = ActionChains(driver)
action.send_keys('calculus').perform()

action = ActionChains(driver)
action.key_down(Keys.ENTER).perform()

driver.find_element_by_css_selector('.s-image').click()
time.sleep(2)
driver.find_element_by_css_selector('#add-to-cart-button').click()

action = ActionChains(driver)
driver.find_element_by_css_selector('.nav-search-field').click()
time.sleep(2)
action.send_keys('geometry').perform()
action = ActionChains(driver)
action.key_down(Keys.ENTER).perform()

time.sleep(2)
driver.find_element_by_css_selector('.s-image').click()
driver.find_element_by_css_selector('#add-to-cart-button').click()

time.sleep(2)
driver.find_element_by_css_selector('.a-button-inner').click()

driver.close()