import win32gui
import win32con
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
import time


path = 'D:\OneDrive\桌面\石高林_软件自动化测试.pdf'

# 无法点击 input type='file' 需使用 71 版本驱动
driver = webdriver.Chrome(r'D:\webdriver\chromedriver_71.exe')
driver.maximize_window()
# driver.implicitly_wait(10)
wait = WebDriverWait(driver, 10)
driver.get('file:///D:/OneDrive/%E6%A1%8C%E9%9D%A2/upload.html')
element_upload = wait.until(ec.element_to_be_clickable((By.ID, 'upload')))
element_upload.click()
time.sleep(1)
# 打开一级窗口
dialog = win32gui.FindWindow('#32770', '打开')
# 二级窗口
comboBoxEx32 = win32gui.FindWindowEx(dialog, 0, 'ComboBoxEx32', None)
# 三级窗口
comboBox = win32gui.FindWindowEx(comboBoxEx32, 0, 'ComboBox', None)
# 四级窗口
edit = win32gui.FindWindowEx(comboBox, 0, 'Edit', None)
# 打开
button = win32gui.FindWindowEx(dialog, 0, 'Button', None)
time.sleep(1)
# 选中文件
win32gui.SendMessage(edit, win32con.WM_SETTEXT, None, path)
time.sleep(1)
# 单击打开，选择文件
win32gui.SendMessage(dialog, win32con.WM_COMMAND, 1, button)
