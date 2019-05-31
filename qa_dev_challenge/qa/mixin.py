from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

def hover(browser, element):
    hover = ActionChains(browser).move_to_element(element)
    hover.perform()

def wait_presense_xpath(browser, xpath):
	WebDriverWait(browser, 30).until(
    	ec.presence_of_element_located((By.XPATH, xpath)))