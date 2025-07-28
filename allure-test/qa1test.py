# -*- coding: utf-8 -*-
"""
-------------------------------------------------
# @Project  :pydemo
# @File     :qa1test
# @Date     :2025/6/23 15:55
# @Author   :zhuzhenzhong
# @Description :allure的step添加步骤描述的用法
-------------------------------------------------
"""
import os
import allure
import pytest


@allure.step("步骤二")
def passing_step():
    pass


@allure.step("步骤三")
def step_with_nested_steps():
    nested_step()


@allure.step("步骤四")
def nested_step():
    nested_step_with_arguments(1, 'abc')


@allure.step("步骤五")
def nested_step_with_arguments(arg1, arg2):
    pass


@allure.step("步骤一")
@allure.title("demo案例")
def test_with_nested_steps():
    passing_step()
    step_with_nested_steps()


if __name__ == '__main__':
    pytest.main(['-s', '-q', 'test_allure04.py', '--clean-alluredir', '--alluredir=allure-results'])
    os.system(r"allure generate ./allure-results -c -o allure-report")
    os.system(r"allure open allure-report")
