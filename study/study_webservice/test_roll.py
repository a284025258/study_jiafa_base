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
element_link = driver.find_element_by_xpath('//*/img[@src="./images/public.png"]')
# 1. 滚动到指定元素可见
# element_link.location_once_scrolled_into_view
# 2. 通过 js 指令来滚动
driver.execute_script('arguments[0].scrollIntoView(false);', element_link)
# 3. window.scrollTo(1146,726);
time.sleep(5)
driver.quit()