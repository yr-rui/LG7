import os

from lesson5.pages.main_page import MainPage


class TestImportContact:
    #从首页导入
    def test_import_contact1(self):
        file_path=os.path.abspath("../files/通讯录批量导入模板.xlsx")
        self.main_page=MainPage().goto_contact_page().del_all_contact().goto_main_page()
        contact_dict=self.main_page.goto_import_contact_page().import_contact(file_path).get_contact()
        assert ("18782950693","test2") in contact_dict.items()
    #从通讯录页导入
    def test_import_contact(self):
        file_path=os.path.abspath("../files/通讯录批量导入模板.xlsx")
        self.contact_page=MainPage().goto_contact_page().del_all_contact()
        contact_dict=self.contact_page.goto_import_contact_page().import_contact(file_path).get_contact()
        assert ("18782950693","test2") in contact_dict.items()