import time

from selenium.webdriver.common.by import By

from lesson5.pages.add_member_page import AddMemberPage
from lesson5.pages.base_page import BasePage
from lesson5.pages.contact_page import ContactPage
from lesson5.pages.import_contact_page import ImportContactPage


class MainPage(BasePage):
    def goto_contact_page(self):
        self.contact=(By.ID,"menu_contacts")
        self.find_element(self.contact).click()
        # self.driver.find_element_by_id("menu_contacts").click()
        time.sleep(1)
        return ContactPage(self.driver)
    def goto_add_member_page(self):
        self.driver.find_element_by_css_selector(".index_service_cnt_itemWrap:nth-child(1)>div").click()
        time.sleep(1)
        return AddMemberPage(self.driver)
    def goto_import_contact_page(self):
        self.driver.find_element_by_css_selector(".index_service_cnt_itemWrap:nth-child(2)>div").click()
        time.sleep(1)
        return ImportContactPage(self.driver)