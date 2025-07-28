# -*- coding: utf-8 -*-
"""
-------------------------------------------------
# @Project  :myPytestProject
# @File     :db_test
# @Author   :zhuzhenzhong
# @Description :
-------------------------------------------------
"""

import httpx
from utils.assert_utils import AssertUtils
from utils.db_utils import DBUtils
import pytest

@pytest.fixture
def client():
    return httpx.Client(base_url="https://jsonplaceholder.typicode.com")


@pytest.fixture
def assert_utils():
    return AssertUtils()


@pytest.fixture
def db_utils():
    return DBUtils()


def test_get_user_and_assert(client, assert_utils, db_utils):
    response = client.get("/users/1")
    # 接口断言
    assert_utils.assert_status_code(response, 200)
    assert_utils.assert_json_key(response, "name")
    assert_utils.assert_json_value(response, "id", 1)
    # 数据库断言（假设我们有对应的用户表）
    user_id = 1
    sql = f"SELECT nickname FROM user WHERE id = {user_id}"
    assert_utils.assert_db_value(db_utils, sql, "abc1")
    # 最终验证所有断言是否成功
    assert_utils.assert_all()