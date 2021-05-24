import pytest
import yaml

from lesson5.pages.main_page import MainPage

def get_datas():
    with open("../datas/testdata.yaml") as f:
        datas=yaml.safe_load(f)
    return datas

class TestAddMember:
    #从首页添加成员
    # @pytest.mark.parametrize("name,account,phone",[("yuerui","0002","18782950699"),])
    @pytest.mark.parametrize("name,account,phone",get_datas()["member"])
    def test_add_member1(self,name,account,phone):
        self.main_page=MainPage().goto_contact_page().del_all_contact().goto_main_page()
        contact_dict=self.main_page.goto_add_member_page().add_member(name,account,phone).get_contact()
        assert (phone,name) in contact_dict.items()
    #从通讯录页添加成员
    @pytest.mark.parametrize("name,account,phone",get_datas()["member"])
    def test_add_member2(self,name,account,phone):
        self.contact_page=MainPage().goto_contact_page().del_all_contact()
        contact_dict=self.contact_page.goto_add_member_page().add_member(name,account,phone).get_contact()
        assert (phone, name) in contact_dict.items()



