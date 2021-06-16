import time

from appium.webdriver.common.mobileby import MobileBy

from lesson6.pages.base_page import BasePage

class ContactInfoEditPage(BasePage):
    def delete_contact(self):
        from lesson6.pages.contact_page import ContactPage
        self.log("滑动点击删除成员，弹框确认，返回通讯录页面")
        self.swipe_find(MobileBy.XPATH,"//*[@text='删除成员']").click()
        self.find(MobileBy.XPATH,"//*[@text='确定']").click()
        time.sleep(5)
        return ContactPage(self._driver)