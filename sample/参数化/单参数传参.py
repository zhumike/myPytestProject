# -*- coding: utf-8 -*-
# @Time : 2022/11/29 2:36 下午
# @Author : zhuzhenzhong
# import pytest
#
# data1 = [('demo1', 'hello'), ('demo2', 'world')]
#
# # 只有一个参数接收数据
# @pytest.mark.parametrize("login", data1)
# def test_demo(login):
#     print(login)
#
#
# if __name__ == '__main__':
#     pytest.main(['-s', 'test_login.py'])

import pytest
test_user_data = [{"user":"admin1"}, {"user":"admin2"}]


@pytest.fixture()
def login(request):
    user = request.param
    print("登录账户：%s"%user['user'])
    return user


# indirect=True 声明login是函数
@pytest.mark.parametrize("login", test_user_data, indirect=True)
def test_login(login):
    a = login
    print(a)


if __name__ == "__main__":
    pytest.main(["-s", "test.py"])