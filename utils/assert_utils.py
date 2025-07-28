# -*- coding: utf-8 -*-
"""
-------------------------------------------------
# @Project  :pydemo
# @File     :assert_utils
# @Date     :2025/7/12 10:57
# @Author   :zhuzhenzhong
# @Description :断言工具类
-------------------------------------------------
"""

import logging
import json
from typing import Any, Union
logger = logging.getLogger(__name__)
class AssertUtils:
    def __init__(self):
        self._failures = []
    def assert_equal(self, actual: Any, expected: Any, msg: str = "") -> None:
        try:
            assert actual == expected, f"{msg} | Expected: {expected}, Actual: {actual}"
        except AssertionError as e:
            self._failures.append(str(e))
            logger.error(f"断言失败: {e}")
    def assert_in(self, actual: str, expected: str, msg: str = "") -> None:
        try:
            assert expected in actual, f"{msg} | Expected substring '{expected}' not in '{actual}'"
        except AssertionError as e:
            self._failures.append(str(e))
            logger.error(f"断言失败: {e}")
    def assert_status_code(self, response, expected_code: int) -> None:
        self.assert_equal(response.status_code, expected_code, "HTTP 状态码不匹配")
    def assert_json_key(self, response, key: str) -> None:
        try:
            json_data = response.json()
            assert key in json_data, f"JSON 响应缺少字段: {key}"
        except Exception as e:
            self._failures.append(str(e))
            logger.error(f"断言失败: {e}")
    def assert_json_value(self, response, key: str, expected_value: Any) -> None:
        try:
            json_data = response.json()
            actual_value = json_data.get(key)
            assert actual_value == expected_value, f"JSON 字段值不匹配: {key} | Expected: {expected_value}, Actual: {actual_value}"
        except Exception as e:
            self._failures.append(str(e))
            logger.error(f"断言失败: {e}")
    def assert_db_value(self, db_utils, sql: str, expected_value: Any) -> None:
        try:
            result = db_utils.query(sql)
            actual_value = result[0] if result else None
            assert actual_value == expected_value, f"数据库值不匹配 | SQL: {sql} | Expected: {expected_value}, Actual: {actual_value}"
        except Exception as e:
            self._failures.append(str(e))
            logger.error(f"断言失败: {e}")
    def assert_all(self):
        if self._failures:
            error_msg = "\n".join(self._failures)
            raise AssertionError(f"以下断言失败:\n{error_msg}")
        else:
            logger.info("所有断言通过")
