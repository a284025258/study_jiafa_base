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
driver.get('file:///D:/OneDrive/%E6%A1%8C%E9%9D%A2/upload.html')
element_upload = driver.find_element_by_id('upload')
# input type='file' 上传框，直接 send_keys 传入文件路径
element_upload.send_keys(r'D:\OneDrive\桌面\石高林_软件自动化测试.pdf')
time.sleep(5)
driver.quit()
