# -*- coding: utf-8 -*-
'''
@Author : zhuzhenzhong
@File : own_check_functions_test.py
'''
import pytest
from pytest_check import check

@check.check_func
def is_four(a):
    assert a == 4


@pytest.mark.parametrize('num', [1, 2, 3,4])
def test_all_four(num):
    is_four(num)


def test_raises():
    with check.raises(AssertionError):
        x = 9
        assert x < 4
