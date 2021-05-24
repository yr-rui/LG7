import time

from selenium.webdriver.common.by import By

from lesson5.pages.base_page import BasePage


class  ContactPage(BasePage):
    def goto_add_member_page(self):
        from lesson5.pages.add_member_page import AddMemberPage
        self.driver.find_element_by_css_selector(".js_has_member a.qui_btn.ww_btn.js_add_member").click()
        time.sleep(1)
        return AddMemberPage(self.driver)
    def goto_add_department_page(self):
        from lesson5.pages.add_department_page import AddDepartmentPage
        self.driver.find_element_by_css_selector(".member_colLeft_top_addBtnWrap").click()
        self.driver.find_element_by_class_name("js_create_party").click()
        time.sleep(1)
        return AddDepartmentPage(self.driver)
    def goto_import_contact_page(self):
        from lesson5.pages.import_contact_page import ImportContactPage
        self.driver.find_element_by_css_selector(".js_has_member div.ww_btn_PartDropdown_left").click()
        self.driver.find_element_by_css_selector(".js_has_member a.js_import_member").click()
        time.sleep(1)
        return ImportContactPage(self.driver)
    def goto_main_page(self):
        self.driver.find_element_by_id("menu_index").click()
        from lesson5.pages.main_page import MainPage
        return MainPage(self.driver)
    def del_all_contact(self):
        self.driver.find_element_by_css_selector("tr.js_title input").click()
        self.driver.find_element_by_css_selector(".qui_btn.ww_btn.js_delete").click()
        self.driver.find_element_by_css_selector("[d_ck=submit]").click()
        time.sleep(1)
        return ContactPage(self.driver)
    def del_depart_name(self,name):
        ele_xpath=f"//div[@class='member_colLeft_bottom']//a[text()='{name}']"
        ele_del_xpath=f"//div[@class='member_colLeft_bottom']//a[text()='{name}']/span"
        print(ele_del_xpath)
        try:
            # 删除最后一个部门self.driver.find_element_by_css_selector("ul[class=jstree-children][role=group]>li:nth-last-child(1) span").click()
            self.driver.find_element_by_xpath(ele_xpath).click()
            self.driver.find_element_by_xpath(ele_del_xpath).click()
            self.driver.find_element_by_xpath("//li/a[text()='删除']").click()
            self.driver.find_element_by_xpath("//a[@d_ck='submit']").click()
        except:
            print("需要删除的部门不存在")
        time.sleep(2)
        return ContactPage(self.driver)

    def get_contact(self):
        name_ele_list = self.driver.find_elements_by_css_selector(".member_colRight_memberTable_td:nth-child(2)")
        name_list = [name.text for name in name_ele_list]
        phone_ele_list=self.driver.find_elements_by_css_selector(".member_colRight_memberTable_td:nth-child(5)")
        phone_list=[phone.text for phone in phone_ele_list]
        contact_dict=dict(zip(phone_list,name_list))
        return contact_dict

    def get_department(self):
        # depart_eles=self.driver.find_elements(By.XPATH,"//a[@tabindex='-1']")
        depart_eles=self.driver.find_elements(By.CSS_SELECTOR,"a.jstree-anchor")
        depart_list=[depart.text for depart in depart_eles]
        print(depart_list)
        return depart_list

