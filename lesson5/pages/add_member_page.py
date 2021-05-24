import time

from selenium.webdriver.common.by import By

from lesson5.pages.base_page import BasePage



class AddMemberPage(BasePage):
    def add_member(self,name,account,phone):
        from lesson5.pages.contact_page import ContactPage
        self.driver.find_element(By.ID,"username").send_keys(name)
        self.driver.find_element(By.ID,"memberAdd_acctid").send_keys(account)
        self.driver.find_element(By.ID,"memberAdd_phone").send_keys(phone)
        #取消发送邀请
        self.driver.find_element(By.NAME,"sendInvite").click()
        #点击保存
        self.driver.find_element(By.CSS_SELECTOR,"a.qui_btn.ww_btn.js_btn_save").click()
        #点击通讯录返回列表页面
        self.driver.find_element(By.ID,"menu_contacts").click()
        time.sleep(1)
        return ContactPage(self.driver)
