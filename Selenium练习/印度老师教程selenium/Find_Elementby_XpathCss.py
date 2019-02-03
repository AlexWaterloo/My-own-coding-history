from selenium import webdriver
class FindByXpathCss():
    def test(self):
        baseUrl="https://learn.letskodeit.com/p/practice"
        driver=webdriver.Chrome("C:\Program Files (x86)\chromedriver_win32\chromedriver.exe")
        driver.get(baseUrl)
        elementByXpath=driver.find_element_by_xpath("//input[@placeholder='Enter Your Name']")
        if elementByXpath is not None:
            print("we found an element by Xpath")
        elementByCss=driver.find_element_by_css_selector("#name")
        if elementByCss is not None:
            print("we found an element by Css")
ff=FindByXpathCss()
ff.test()