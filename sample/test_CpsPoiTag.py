# -*- coding: utf-8 -*-
# @Time : 2021/6/23 2:26 下午
# @Author : zhuzhenzhong

import allure
import pytest
import requests
class TestCpsPoiTag:
    @allure.title("测试http")
    def test_getsuccess(self):
        host = "http://aweme.snssdk.com.boe-gateway.byted.org"
        path = "/aweme/v1/commerce/star/cps/poi/tag/"
        headers = {"X-TT-ENV": "boe_grouponcenter_zhutest", "Cookie": "sessionid=9394c52a74b673cd8a2b10f9eabc475e;"}
        r = requests.request("GET", url=host + path, headers=headers)
        response = r.json()
        print(response)

    @pytest.mark.website
    def test_1(setup_function):
        print('Test_1 called.')
    # assert response
