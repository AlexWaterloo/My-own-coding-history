from selenium import webdriver
import time
driver = webdriver.Chrome("C:\Program Files (x86)\chromedriver_win32\chromedriver.exe")
driver.fullscreen_window()
driver.get('http://www.baidu.com')
driver.find_element_by_id('kw').send_keys('this is my own page\n')
driver.save_screenshot('C:/Users\lenovo\Desktop\截图.png')
driver.close()