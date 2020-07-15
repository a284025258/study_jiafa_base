from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
wait = WebDriverWait(driver, 10)
driver.get('https://www.12306.cn')
driver.execute_script('window.open()')
driver.switch_to.window(driver.window_handles[-1])
driver.get('https://www.baidu.com')
time.sleep(5)
driver.quit()
