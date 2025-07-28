# -*- coding: utf-8 -*-
"""
-------------------------------------------------
# @Project  :myPytestProject
# @File     :test_da_cases
# @Author   :zhuzhenzhong
# @Description :
-------------------------------------------------
"""

# -*- coding: utf-8 -*-
'''
@Author : zhuzhenzhong
@File : demo.py
演示用例的初始化和结束时，通用的操作
'''
import pytest
from utils.db_utils import DBUtils
from loguru import logger as loguru_logger


@pytest.fixture(scope='class')
def setup_class():
    print("class setup")
    yield
    print("class end")# 清除测试记录

@pytest.fixture(scope='function')
def setup_function():
    print("方法setup")
    sql = f"SELECT * FROM user  LIMIT 3"
    DbSql = DBUtils()
    data = DbSql.queryMany(sql)
    loguru_logger.info("所有记录数据库信息是：{}",data)
    loguru_logger.info("一条记录数据库信息是：{}",data[0])
    loguru_logger.info("数据字段类型是：{}",type(data[0][0]))

    global a
    a = data[0][0]

    yield
    print("方法end")



class Test_Demo():

    @pytest.mark.usefixtures('setup_function')
    def test_case1(self):
        print("开始执行测试用例1")
        assert 1 + 1 == 2
        assert a in [1,2,3,4,5,6,7]

    def test_case2(self):
        print("开始执行测试用例2")
        assert 2 + 8 == 10
