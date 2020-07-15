from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time


driver = webdriver.Chrome()
driver.maximize_window()
wait = WebDriverWait(driver, 10)
# 创建 ActionChains 对象 初始化动作链条
action = ActionChains(driver)
driver.get('https://www.baidu.com')
element_setting = wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, 'span#s-usersetting-top')))
# 鼠标悬停  调用 perform() 动作才会执行
action.move_to_element(element_setting).perform()
action.click(wait.until(ec.element_to_be_clickable((By.PARTIAL_LINK_TEXT, '高级搜索')))).perform()
wait.until(ec.element_to_be_clickable((By.XPATH, ('//*[@id="adv-setting-ft"]/div/div[1]/span')))).click()
wait.until(ec.element_to_be_clickable((By.XPATH, ('//*/p[@data-value="pdf"]')))).click()
# 创建 Select 对象
# select = Select(wait.until(
#     ec.element_to_be_clickable((By.XPATH, "//*[@id='adv-setting-ft']/div/div[@class='c-select-selection']"))))
# select.select_by_value('pdf')

time.sleep(3)
driver.quit()
