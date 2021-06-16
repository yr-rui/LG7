from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver
from selenium.common.exceptions import NoSuchElementException
import logging


class BasePage:
    logging.basicConfig(level=logging.INFO)
    def __init__(self,driver:WebDriver=None):
        self._driver=driver

    def log(self,info):
        logging.info(info)
    def find(self,by,value):
        self.log(by)
        self.log(value)
        return self._driver.find_element(by,value)
    def swipe_down(self):
        size = self._driver.get_window_size()
        # 'width', 'height'
        width = size['width']
        height = size['height']
        x = width * 0.5
        starty = height * 0.8
        endy = height * 0.2
        self._driver.swipe(x, starty, x, endy, 2000)
    def swipe_find(self,by,value,num=3):
        for i in range(0,num):
            try:
                return self.find(by,value)
            except:
                self.swipe_down()
        raise NoSuchElementException(f"滑动了{num}次，没有找到元素")



