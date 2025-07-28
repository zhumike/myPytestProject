# -*- coding: utf-8 -*-
'''
@Author : zhuzhenzhong
@File : speed_test.py
'''
from pytest_check import check

def test_max_tb():
    check.set_max_tb(2)
    for i in range(1, 11):
        check.equal(i, 100)

def test_max_report():
    check.set_max_report(5)
    for i in range(1, 11):
        check.equal(i, 100)

def test_max_fail():
    check.set_max_fail(5)
    for i in range(1, 11):
        check.equal(i, 100)