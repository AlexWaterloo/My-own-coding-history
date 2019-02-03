from selenium import webdriver
class FindByClassTag():
    def test(self):
        baseUrl="https://learn.letskodeit.com/p/practice"
        driver=webdriver.Chrome("C:\Program Files (x86)\chromedriver_win32\chromedriver.exe")
        driver.get(baseUrl)
        elementByClass=driver.find_element_by_class_name("displayed-class")
        elementByClass.send_keys("Testing the element")

        if elementByClass is not None:
            print("we found an element by Class")
        elementByTag=driver.find_element_by_tag_name("h1")
        elementByTag.click()
        if elementByTag is not None:
            print("we found an element by Tag")
ff=FindByClassTag()
ff.test()