
from lesson5.pages.base_page import BasePage



class ImportContactPage(BasePage):
    def import_contact(self,abspath):
        from lesson5.pages.contact_page import ContactPage
        #sendkeys只支持绝对路径
        self.driver.find_element_by_id("js_upload_file_input").send_keys(abspath)
        self.driver.find_element_by_id("submit_csv").click()
        #导入成功后点击前往查看
        self.driver.find_element_by_id("reloadContact").click()
        return ContactPage(self.driver)