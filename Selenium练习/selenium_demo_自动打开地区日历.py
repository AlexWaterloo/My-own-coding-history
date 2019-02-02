from selenium import webdriver
from selenium.webdriver.support.select import Select
import time
driver=webdriver.Chrome("C:\Program Files (x86)\chromedriver_win32\chromedriver.exe")
driver.fullscreen_window()
driver.get('http://timeanddate.com')
monthelements=driver.find_element_by_id('month')
months=Select(monthelements)
months.select_by_visible_text('December')
countryelements=driver.find_element_by_id('country')
countries=Select(countryelements)
countries.select_by_visible_text('China')
driver.find_element_by_xpath("//input[@value='View Calendar']").click()






