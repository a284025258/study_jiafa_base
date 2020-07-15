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
element_date = driver.find_element_by_id('train_date')
# 准备 js 代码
# arguments[0] 表示占位符 实际为 element_date
js_code = "arguments[0].readonly = false;"
# 执行 js 代码
driver.execute_script(js_code, element_date)
time.sleep(0.5)
driver.execute_script("arguments[0].value = '2020-01-01';", element_date)
# get_attribute('name') 获取定位到的元素的属性
# print(input_box.get_attribute('name'))

time.sleep(5)
driver.quit()