from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from lesson6.pages.base_page import BasePage
from lesson6.pages.contact_page import ContactPage

#首页
class IndexPage(BasePage):
    def goto_contact_page(self):
        self.log("点击通讯录，进入通讯录页面")
        #点击通讯录
        # self.find(MobileBy.XPATH,"//*[@text='通讯录']").click()
        WebDriverWait(self._driver,30).until(lambda x:x.find_element_by_xpath("//*[@text='通讯录']")).click()

        # self._driver.find_element(MobileBy.XPATH,"//*[@text='通讯录']").click()
        # self.find_click(MobileBy.XPATH,"//*[@text='通讯录']")
        return ContactPage(self._driver)