# -*- coding: utf-8 -*-
# @Time : 2022/11/29 2:34 下午
# @Author : zhuzhenzhong

import pytest
test_user_data = [{"user":"admin1"}, {"user":"admin2"}]


@pytest.fixture(params=test_user_data)
def login(request):
    user = request.param
    print("登录账户：%s"%user['user'])
    return user
def test_login(login):
    login


if __name__ == "__main__":
    pytest.main(["-s", "test_01.py"])