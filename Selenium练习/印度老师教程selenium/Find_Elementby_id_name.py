from selenium import webdriver
class FindByIdName():
    def test(self):
        baseUrl="https://learn.letskodeit.com/p/practice"
        driver=webdriver.Chrome("C:\Program Files (x86)\chromedriver_win32\chromedriver.exe")
        driver.get(baseUrl)
        elementById=driver.find_element_by_id("name")
        if elementById is not None:
            print("we found an element by Id")
        elementByName=driver.find_element_by_name("enter-name")
        if elementByName is not None:
            print("we found an element by name")
        elementByName.click()
ff=FindByIdName()
ff.test()