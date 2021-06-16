import pytest
import yaml

from lesson6.pages.app import App

def get_datas():
    with open("./contact.yaml") as f:
        datas=yaml.safe_load(f)
    return datas


class TestContact:
    def setup_class(self):
        self.app=App()
    def setup(self):
        self.main=self.app.start().goto_main()
        self.contact=self.main.goto_contact_page()
    def teardown_class(self):
        self.app.stop()
    @pytest.mark.parametrize("name,phone",[(i['name'], i['phone']) for i in get_datas()])
    def test_add_contact(self,name,phone):
        # self.contact=self.main.goto_contact_page()
        self.contact.goto_add_contact_page().goto_edit_contact_page().add_contact(name,phone).verify_ok()

    # @pytest.mark.parametrize("name",['test1',])
    @pytest.mark.parametrize("name",[i['name'] for i in get_datas()])
    def test_delete_contact(self,name):
        current_contact=self.contact.goto_contact_info_page(name).goto_contact_info_setting_page().goto_contact_info_edit_page().delete_contact()
        # assert False==current_contact.swipe_find_contact(name)
        assert f"{name}不在通讯录中"==current_contact.swipe_find_contact(name)

