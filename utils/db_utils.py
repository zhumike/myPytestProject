# -*- coding: utf-8 -*-
"""
-------------------------------------------------
# @Project  :myPytestProject
# @File     :db_utils
# @Author   :zhuzhenzhong
# @Description :
-------------------------------------------------
"""


import pymysql
from configs.db_config import DB_CONFIG
class DBUtils:
    def __init__(self, db_config=None):
        self.db_config = db_config or DB_CONFIG
        self.connection = None
    def connect(self):
        self.connection = pymysql.connect(**self.db_config)
        return self.connection.cursor()
    def query(self, sql: str):
        cursor = self.connect()
        try:
            cursor.execute(sql)
            result = cursor.fetchone() if "SELECT" or"INTO" in sql.upper() else None
            self.connection.commit()
            return result
        finally:
            cursor.close()
            self.connection.close()

    def queryMany(self, sql: str):
        cursor = self.connect()
        try:
            cursor.execute(sql)
            result = cursor.fetchall() if "SELECT" or"INTO" in sql.upper() else None
            self.connection.commit()
            return result
        finally:
            cursor.close()
            self.connection.close()


    def execute(self, sql: str):
        cursor = self.connect()
        try:
            cursor.execute(sql)
            self.connection.commit()
        finally:
            cursor.close()
            self.connection.close()