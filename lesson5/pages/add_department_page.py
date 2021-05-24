import time

from selenium.webdriver.common.by import By

from lesson5.pages.base_page import BasePage



class AddDepartmentPage(BasePage):
    def add_department(self,name):
        from lesson5.pages.contact_page import ContactPage
        self.driver.find_element(By.CSS_SELECTOR,"input[name=name]").send_keys(name)
        self.driver.find_element(By.XPATH,"//div[@class='member_tag_dialog_inputDlg']//div[1]/label").click()
        time.sleep(1)
        #选择所属部门
        self.driver.find_element(By.CSS_SELECTOR,".qui_btn.ww_btn.ww_btn_Dropdown.js_toggle_party_list").click()
        self.driver.find_element(By.XPATH,"//div[@class='member_tag_dialog_inputDlg']//a[@id='1688854580231431_anchor']").click()
        #保存
        self.driver.find_element(By.XPATH,"//a[@d_ck='submit']").click()
        time.sleep(1)
        return ContactPage(self.driver)
