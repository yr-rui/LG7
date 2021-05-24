from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:
    def __init__(self,driver:WebDriver=None):
        if driver is not None:
            self.driver=driver
        else:
            options=webdriver.ChromeOptions()
            options.debugger_address="127.0.0.1:9222"
            self.driver=webdriver.Chrome(options=options)
            self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        self.driver.implicitly_wait(5)
    def find_element(self,locator):
        return self.driver.find_element(*locator)
