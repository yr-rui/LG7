import pytest

from lesson4.calculator import Calculator


@pytest.fixture(scope="class")
def calcu():
    print("开始计算")
    cal = Calculator()
    #yield可以激活teardown操作
    yield cal
    print("结束计算")