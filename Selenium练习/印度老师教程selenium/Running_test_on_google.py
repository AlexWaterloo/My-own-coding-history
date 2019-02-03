from selenium import webdriver
import os
class RunChromeTest():
    def test(self):
        # driverlocation="C:\Program Files (x86)\chromedriver_win32\chromedriver.exe"
        # os.environ["webdriver.chrome.driver"]=driverlocation
        driver=webdriver.Chrome("C:\Program Files (x86)\chromedriver_win32\chromedriver.exe")
        driver.get("http://amazon.com")
chrometest=RunChromeTest()
chrometest.test()
