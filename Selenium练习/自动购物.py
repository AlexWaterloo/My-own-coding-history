from selenium import webdriver
from selenium.webdriver.support.select import Select
import time
driver = webdriver.Chrome("C:\Program Files (x86)\chromedriver_win32\chromedriver.exe")
driver.fullscreen_window()
driver.get('http://automationpractice.com/index.php')
driver.find_element_by_xpath("//a[@title='Log in to your customer account']").click()
driver.find_element_by_xpath("//input[@id='email']").send_keys("zqwaterloo@gmail.com")
driver.find_element_by_xpath("//input[@id='passwd']").send_keys("zhangqing123")
driver.find_element_by_xpath("//button[@name='SubmitLogin']//span[1]").click()
driver.find_element_by_xpath("//span[contains(text(),'Home')]").click()
driver.implicitly_wait(5)
driver.find_element_by_xpath("//li[@class='ajax_block_product col-xs-12 col-sm-4 col-md-3 first-in-line first-item-of-tablet-line first-item-of-mobile-line']//a[@title='Faded Short Sleeve T-shirts'][contains(text(),'Faded Short Sleeve T-shirts')]").click()
driver.find_element_by_xpath("//span[contains(text(),'Add to cart')]").click()
driver.find_element_by_xpath("//div[@class='button-container']//span[1]//span[1]").click()
driver.find_element_by_xpath("//a[@title='Log me out']").click()
time.sleep(5)
driver.quit()