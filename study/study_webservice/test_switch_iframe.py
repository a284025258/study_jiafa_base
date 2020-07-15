from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
import time

def login_qq_mail():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get('https://mail.qq.com')
    wait = WebDriverWait(driver, 10)
    # frame_to_be_available_and_switch_to_it() 可传参数[1.index 2.name 3.webelement对象 4.locator] 当......可用时，定位并切换到 iframe
    wait.until(ec.frame_to_be_available_and_switch_to_it((By.NAME, 'login_frame')))
    wait.until(ec.visibility_of_element_located((By.ID, 'switcher_plogin'))).click()
    wait.until(ec.visibility_of_element_located((By.ID, 'u'))).send_keys('284025258@qq.com')
    wait.until(ec.visibility_of_element_located((By.ID, 'p'))).send_keys('sgl17612831881..')
    driver.find_element_by_id('login_button').click()
    time.sleep(3)
    print(driver.title)
    driver.quit()

# 重试
while True:
    try:
        login_qq_mail()
        break
    except TimeoutException:
        login_qq_mail()
