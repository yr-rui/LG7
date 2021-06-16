from appium.webdriver.common.mobileby import MobileBy

from lesson6.pages.base_page import BasePage
from lesson6.pages.contact_info_setting_page import ContactInfoSettingPage


class ContactInfoPage(BasePage):
    def goto_contact_info_setting_page(self):
        self.log("点击...更多按钮,进入个人信息设置页面")
        settings=self.find(MobileBy.XPATH,"//*[@text='个人信息']/../../../../../android.widget.LinearLayout[2]//android.widget.TextView")
        settings.click()
        return ContactInfoSettingPage(self._driver)
