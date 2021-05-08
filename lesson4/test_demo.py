"""1、将课上的计算器的相加相除功能 ，完善测试用例，使用fixture 实现 setup_class/teardown_class 功能（使用conftest.py文件保存 fixture）
2、添加测试步骤，生成测试报告，截图回复课程贴
"""
import allure
import pytest
import yaml

def get_datas():
    with open("datas/data.yaml") as f:
        datas=yaml.safe_load(f)
    return datas

@allure.feature("测试计算器中的加法")
class TestCalAdd:

    @pytest.mark.parametrize("a,b,expect",get_datas()["add_int"]["datas"])
    @allure.story("测试整数相加")
    def test_add_int(self,calcu,a,b,expect):
        with allure.step(f"测试{a}+{b}是否等于{expect}"):
            assert expect==calcu.add(a,b)

    @pytest.mark.parametrize("a,b,expect",get_datas()["add_float"]["datas"],ids=get_datas()["add_float"]["ids"])
    @allure.story("测试小数相加")
    def test_add_float(self,calcu,a,b,expect):
        assert expect==round(calcu.add(a,b),2)

    @pytest.mark.parametrize("a,b,expect",get_datas()["add_minus"]["datas"])
    @allure.story("测试负数相加")
    def test_add_minus(self,calcu,a,b,expect):
        assert expect==calcu.add(a,b)

    # @pytest.mark.parametrize("a,b,expect",get_datas()["add_fraction"]["datas"],ids=get_datas()["add_fraction"]["ids"])
    #这里yaml中的分数取出来自动变成字符串了，又不能转换成数字格式，导致无法计算
    @pytest.mark.parametrize("a,b,expect",[[1/3,1/3,2/3],[1/3,1/4,7/12]],ids=["fraction1","fraction2"])
    @allure.story("测试分数相加")
    def test_add_fraction(self,calcu,a,b,expect):
        with allure.step("计算和"):
            sum=calcu.add(a, b)
        with allure.step("与期望值进行对比验证"):
            assert round(expect,4)==round(sum,4)

    @pytest.mark.parametrize("a,b",get_datas()["add_error"]["datas"])
    @allure.story("测试加数中有非数字")
    def test_add_error(self,calcu,a,b):
        try:
            calcu.add(a,b)
        except TypeError:
            print("加数的数据类型不正确，只能为数字")

@allure.feature("测试计算器中的除法")
class TestCalDiv:
    @allure.story("整数除法")
    @pytest.mark.parametrize("a,b,expect,step",get_datas()["div_int"]["datas"],ids=get_datas()["div_int"]["ids"])
    def test_div_int(self,calcu,a,b,expect,step):
        with allure.step(step):
            assert expect==round(calcu.div(a,b),3)


    @pytest.mark.parametrize("a,b,expect,step",get_datas()["div_float"]["datas"],ids=get_datas()["div_float"]["ids"])
    @allure.story("小数除法")
    def test_div_float(self,calcu,a,b,expect,step):
        with allure.step(step):
            assert expect==round(calcu.div(a,b),2)

    @allure.story("负数除法")
    @pytest.mark.parametrize("a,b,expect,step",get_datas()["div_minus"]["datas"])
    def test_div_minus(self,calcu,a,b,expect,step):
        with allure.step(step):
            assert expect==calcu.div(a,b)


    @allure.story("异常场景")
    @pytest.mark.parametrize("a,b,step",get_datas()["div_error"]["datas"])
    def test_div_error(self,calcu,a,b,step):
        with allure.step(step):
            with pytest.raises(Exception):
                calcu.div(a,b)





