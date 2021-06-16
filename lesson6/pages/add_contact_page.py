from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait

from lesson6.pages.base_page import BasePage
from lesson6.pages.edit_contact_page import EditContactPage


class AddContactPage(BasePage):
    def goto_edit_contact_page(self):
        self.log("点击手动输入添加,进入编辑联系人页面")
        self.find(MobileBy.XPATH, "//*[@text='手动输入添加']").click()
        return EditContactPage(self._driver)
    def verify_ok(self):
        self.log("出现添加成功提示")
        WebDriverWait(self._driver,10).until(lambda x:x.find_element(MobileBy.XPATH,"//*[@text='添加成功']"))
