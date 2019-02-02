from selenium import webdriver
import time
driver=webdriver.Chrome("C:\Program Files (x86)\chromedriver_win32\chromedriver.exe")
driver.fullscreen_window()
driver.get('http://baidu.com')
time.sleep(2)#休息2秒
driver.minimize_window()#最小化窗口
baidu_title=driver.title#赋值title
print(baidu_title)
url=driver.current_url#获取当前url
print(url)
driver.fullscreen_window()
time.sleep(2)
driver.refresh()
driver.get("http://google.com")
time.sleep(2)
driver.back()
time.sleep(2)
# driver.forward()
page_source=driver.page_source
print(page_source)







# driver.close()