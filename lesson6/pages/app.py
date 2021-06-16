from appium import webdriver

from lesson6.pages.base_page import BasePage
from lesson6.pages.index_page import IndexPage


class App(BasePage):
    def start(self):
        self.log("启动app")
        if self._driver is None:
            print("初始化driver")
            caps={}
            caps['platformName']='android'
            caps['deviceName']='emulator-5554'
            caps['appPackage']='com.tencent.wework'
            caps['appActivity']='.launch.WwMainActivity'
            caps['noReset']='true'
            self._driver=webdriver.Remote('http://localhost:4723/wd/hub',caps)
            self._driver.implicitly_wait(10)
        else:
            print("复用driver")
            self.restart()
        return self
    def restart(self):
        self.log("重启app")
        self._driver.close_app()
        self._driver.launch_app()
    def stop(self):
        self.log("退出app")
        self._driver.quit()
    def goto_main(self):
        self.log("进入首页")
        return IndexPage(self._driver)
