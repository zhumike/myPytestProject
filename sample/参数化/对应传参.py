# -*- coding: utf-8 -*-
# @Time : 2022/11/29 2:35 下午
# @Author : zhuzhenzhong
import pytest

data1 = [('demo1', 'hello'), ('demo2', 'world')]


@pytest.mark.parametrize("name,password", data1)
def test_demo(name, password):
    print(name, password)


if __name__ == '__main__':
    pytest.main(['-s', 'test_login.py'])