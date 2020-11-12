from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import pyautogui
import time

driver = webdriver.Chrome()
url = "https://youtube.com"
driver.get(url)
driver.maximize_window()
action = ActionChains(driver)

driver.find_element_by_class_name('ytd-searchbox-spt').click()
time.sleep(2)
action.send_keys('iphone 12').perform()

action = ActionChains(driver)
action.key_down(Keys.ENTER).perform()
action.reset_actions()

time.sleep(2)
action = ActionChains(driver)
driver.get('https://www.youtube.com/watch?v=cnXapYkboRQ')
action.send_keys('k').perform()

time.sleep(4)
action = ActionChains(driver)
action.send_keys()


# driver.get('https://accounts.google.com/ServiceLogin/identifier?service=youtube&uilel=3&passive=true&continue=https%3A%2F%2Fwww.youtube.com%2Fsignin%3Faction_handle_signin%3Dtrue%26app%3Ddesktop%26hl%3Dko%26next%3Dhttps%253A%252F%252Fwww.youtube.com%252F&hl=ko&ec=65620&flowName=GlifWebSignIn&flowEntry=AddSession')

# time.sleep(2)

# action.send_keys('ghkrzkdlf@gmail.com').perform()
# action.reset_actions()

# time.sleep(2)

# action = ActionChains(driver)

# driver.find_element_by_class_name('VfPpkd-RLmnJb').click()
# time.sleep(2)
# action.send_keys('ghkrwo321').perform()
# action.reset_actions()
# time.sleep(2)

# driver.find_element_by_class_name('VfPpkd-RLmnJb').click()

# time.sleep(2)

# driver.find_element_by_class_name('title.style-scope.ytd-guide-entry-renderer').click()