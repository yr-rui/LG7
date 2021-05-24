import pytest
import yaml

from lesson5.pages.main_page import MainPage

def get_datas():
    with open("../datas/testdata.yaml") as f:
        datas=yaml.safe_load(f)
    return datas

class TestAddDepartment:
    #添加部门
    @pytest.mark.parametrize("name",get_datas()["department"])
    def test_add_department(self,name):
        self.contact_page=MainPage().goto_contact_page().del_depart_name(name)
        depart_list=self.contact_page.goto_add_department_page().add_department(name).get_department()
        assert name in depart_list

