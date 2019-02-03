from selenium import webdriver
import time
class FindByIdLinkText():
    def test(self):
        baseUrl="https://learn.letskodeit.com/p/practice"
        driver=webdriver.Chrome("C:\Program Files (x86)\chromedriver_win32\chromedriver.exe")
        driver.fullscreen_window()
        driver.get(baseUrl)
        elementByLinkText=driver.find_element_by_link_text("Login")
        if elementByLinkText is not None:
            print("we found an element by link_text")
        elementByPartialLinkText=driver.find_element_by_partial_link_text("Pract")
        if elementByPartialLinkText is not None:
            print("we found an element by partial_lin k_text")
        time.sleep("1")
ff=FindByIdLinkText()
ff.test()