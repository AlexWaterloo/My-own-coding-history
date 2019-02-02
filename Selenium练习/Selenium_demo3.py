from selenium import webdriver

driver = webdriver.Chrome("C:\Program Files (x86)\chromedriver_win32\chromedriver.exe")
driver.fullscreen_window()

# driver.get('http://douban.com')
# driver.find_element_by_class_name('lnk-movie').click()


driver.get("http://automationpractice.com/index.php")
driver.find_element_by_xpath("//a[@title='Contact Us']").click()

driver.get('http://baidu.com')
driver.find_element_by_css_selector('#kw').send_keys("如何找工作\n")

