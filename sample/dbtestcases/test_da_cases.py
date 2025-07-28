# -*- coding: utf-8 -*-
"""
-------------------------------------------------
# @Project  :myPytestProject
# @File     :test_da_cases
# @Author   :zhuzhenzhong
# @Description :
-------------------------------------------------
"""

# -*- coding: utf-8 -*-
'''
@Author : zhuzhenzhong
@File : demo.py
演示用例的初始化和结束时，通用的操作
'''
import pytest

@pytest.fixture(scope='class')
def setup_class():
    print("class setup")
    yield
    print("class end")# 清除测试记录

@pytest.fixture(scope='function')
def setup_function():
    print("方法setup")
    yield
    print("方法end")

class Test_Demo():

    @pytest.mark.usefixtures('setup_function')
    def test_case1(self):
        print("开始执行测试用例1")
        assert 1 + 1 == 2

    def test_case2(self):
        print("开始执行测试用例2")
        assert 2 + 8 == 10
