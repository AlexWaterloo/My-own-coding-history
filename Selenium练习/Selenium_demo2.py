from selenium import webdriver

driver = webdriver.Chrome("C:\Program Files (x86)\chromedriver_win32\chromedriver.exe")
driver.fullscreen_window()

driver.get('http://baidu.com')
elments=driver.find_elements_by_tag_name('a')
for i in elments:
    if "视频"in i.text:
        i.click()

