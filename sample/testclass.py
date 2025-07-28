# -*- coding: utf-8 -*-
# @Time : 2021/6/22 5:00 下午
# @Author : zhuzhenzhong
import allure

class TestClass:
    @allure.title("step1")
    def test_one(self):
        x = "this"
        assert 'h' in x

    def test_two(self):
        x = "hello"
        assert hasattr(x, 'check')
