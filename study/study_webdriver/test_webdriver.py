import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium import webdriver


driver = webdriver.Chrome()
driver.maximize_window()
# 创建显式等待对象
wait = WebDriverWait(driver, 10)
driver.get('https://www.baidu.com')
# visibility_of_element_located 当......可见时定位
wait.until(ec.visibility_of_element_located((By.ID, 'kw'))).send_keys('柠檬班')
# element_to_be_clickable 当......可被点击时定位
wait.until(ec.element_to_be_clickable((By.ID, 'su'))).click()
# 获取当前窗口句柄
windows = driver.window_handles
wait.until(ec.visibility_of_element_located((By.PARTIAL_LINK_TEXT, '柠檬班'))).click()
# 当窗口被打开之前，显式等待  new_window_is_opened(windows) windows: 新窗口打开之前，所有的 handles
wait.until(ec.new_window_is_opened(windows))
# 获取窗口打开后的窗口句柄
windows = driver.window_handles
# 切换最新窗口
driver.switch_to.window(windows[-1])
# presence_of_element_located 当......存在时定位
element2 = wait.until(ec.presence_of_element_located((By.CSS_SELECTOR, 'a.teacher-face-a')))
print(element2)
driver.quit()