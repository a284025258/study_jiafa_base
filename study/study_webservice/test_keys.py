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
# 创建 ActionChains 对象 初始化动作链条
action = ActionChains(driver)
driver.get('https://www.baidu.com')
input_box = driver.find_element_by_id('kw')
input_box.send_keys('lemon')
# 全选 alt + a
input_box.send_keys(Keys.CONTROL, 'a')
# 复制
input_box.send_keys(Keys.CONTROL, 'c')
# 向右移动1格光标
input_box.send_keys(Keys.ARROW_RIGHT)
# 粘贴
input_box.send_keys(Keys.CONTROL, 'v')
# element_setting = wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, 'span#s-usersetting-top')))
# 鼠标悬停  调用 perform() 动作才会执行
# action.move_to_element(element_setting).perform()
# action.click(wait.until(ec.element_to_be_clickable((By.PARTIAL_LINK_TEXT, '高级搜索')))).perform()
# wait.until(ec.element_to_be_clickable((By.XPATH, ('//*[@id="adv-setting-ft"]/div/div[1]/span')))).click()
# wait.until(ec.element_to_be_clickable((By.XPATH, ('//*/p[@data-value="pdf"]')))).click()


time.sleep(5)
driver.quit()
