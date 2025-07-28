# -*- coding: utf-8 -*-
# @Time : 2022/11/29 2:38 下午
# @Author : zhuzhenzhong
import pytest

data1 = ['demo1', 'demo2','demo3']
data2 = ['hello', 'world']

@pytest.mark.parametrize("name1", data1)
@pytest.mark.parametrize("name2", data2)
def test_demo(name1, name2):
    print(name1, name2)

if __name__ == '__main__':
    pytest.main(['-s', 'test_login.py'])