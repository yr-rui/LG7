from appium.webdriver.common.mobileby import MobileBy

from lesson6.pages.base_page import BasePage
class EditContactPage(BasePage):
    def add_contact(self,name,phone):
        from lesson6.pages.add_contact_page import AddContactPage
        self.log("输入信息，点击保存，返回添加联系人页面")
        self.find(MobileBy.XPATH,"//*[contains(@text,'姓名')]/../android.widget.EditText").send_keys(name)
        self.find(MobileBy.XPATH,"//*[contains(@text,'手机')]/..//*[@text='必填']").send_keys(phone)
        self.find(MobileBy.XPATH,"//*[@text='保存']").click()
        return AddContactPage(self._driver)