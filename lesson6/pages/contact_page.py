from appium.webdriver.common.mobileby import MobileBy
from selenium.common.exceptions import NoSuchElementException

from lesson6.pages.add_contact_page import AddContactPage
from lesson6.pages.base_page import BasePage
from lesson6.pages.contact_info_page import ContactInfoPage


class ContactPage(BasePage):
    def goto_add_contact_page(self):
        self.log("滑动点击添加成员按钮,进入添加成员页面")
        self.swipe_find(MobileBy.XPATH,"//*[@text='添加成员']").click()
        return AddContactPage(self._driver)
    def swipe_find_contact(self,name):
        #滑动查找，页面出现添加成员按钮说明已滑动到底部
        self.log("滑动查找成员")
        while True:
            try:
                #如果找到成员了，则将成员的元素返回
                return self.find(MobileBy.XPATH,f"//*[@text='{name}']")
            except:
                try:
                    self.find(MobileBy.XPATH,"//*[@text='添加成员']")
                    return f"{name}不在通讯录中"
                except:
                    self.swipe_down()
    def goto_contact_info_page(self,name):
        self.log("滑动查找成员并点击，进入成员详情页面")
        self.swipe_find_contact(name).click()
        return ContactInfoPage(self._driver)
