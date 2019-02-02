from selenium import webdriver
import time
driver = webdriver.Chrome("C:\Program Files (x86)\chromedriver_win32\chromedriver.exe")
driver.fullscreen_window()
# driver.get('http://amazon.com')
# # driver.find_element_by_id('nav-your-amazon').click()
driver.get('http://google.com')
# driver.find_element_by_id()
# driver.find_element_by_name('q').send_keys('inty youtube demo\n')
# time.sleep(5)
# driver.quit()
driver.find_element_by_link_text('Gmail').click()
driver.back()
driver.find_element_by_partial_link_text('mail').click()