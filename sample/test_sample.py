# -*- coding: utf-8 -*-
# @Time : 2021/6/22 3:48 下午
# @Author : zhuzhenzhong
import allure
import pytest
from datetime import datetime, timedelta


testdata = [
    (datetime(2001, 12, 12), datetime(2001, 12, 11), timedelta(1)),
    (datetime(2001, 12, 11), datetime(2001, 12, 12), timedelta(-1)),
]



@pytest.mark.webtest
def test_sample():
    my_name = "zhaoyue.1985"
    expect_name = "zhaoyue"
    assert my_name == expect_name, "my_name should be " + expect_name
@pytest.mark.webtest
def test_sample2():
    my_name = "zzzz"
    expect_name = "zzzz"
    assert my_name == expect_name


@allure.title("参数化测试")
@pytest.mark.parametrize("a,b,expected", testdata)
def test_timedistance_v0(a, b, expected):
    diff = a - b
    assert diff == expected