from appium.webdriver.common.mobileby import MobileBy

from lesson6.pages.base_page import BasePage
from lesson6.pages.contact_info_edit_page import ContactInfoEditPage


class ContactInfoSettingPage(BasePage):
    def goto_contact_info_edit_page(self):
        self.log("点击编辑成员,进入个人信息编辑页面")
        self.find(MobileBy.XPATH,"//*[@text='编辑成员']").click()
        return ContactInfoEditPage(self._driver)
