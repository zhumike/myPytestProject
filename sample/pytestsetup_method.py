# -*- coding: utf-8 -*-
# @Time : 2021/8/26 2:09 下午
#待重新设计
# @Author : zhuzhenzhong

import pytest


def setup_function():
    print("初始化。。。")

def teardown_function():
    print("清理。。。")

class Test_Demo():
    def test_case1(self):
        print("开始执行测试用例1")
        assert 1 + 1 == 2

    def test_case2(self):
        print("开始执行测试用例2")
        assert 2 + 8 == 10

    def test_case3(self):
        print("开始执行测试用例3")
        assert 99 + 1 == 100