# -*- coding: utf-8 -*-
# @Time : 2021/6/23 2:55 下午
# @Author : zhuzhenzhong
import requests
import pytest

#配置测试url
class UrlData(object):
    def __init__(self):
        self.tltle_url='http://httpbin.org/json'
        self.name_url='https://postman-echo.com/get'

#请求会遍历调用params列表里的每个值
@pytest.fixture(params=[{'name':'lin'},{'name':'huang'}])
def test_data(request):
    return request.param

#测试类
class TestClass(object):
    #前置方法，先初始化测试url
    @pytest.fixture(scope='session')
    def ud(self):
        return UrlData()

    #对接口title_url进行功能测试
    def test_title(self,ud):
        resp=requests.get(ud.tltle_url)
        assert resp.status_code==200,'HTTP返回码不等于200'
        assert resp.json().get('slideshow').get('title')=='Sample Slide Show','标题与预期值不符'

    #对接口name_url进行功能测试
    def test_name(self,ud,test_data):
        resp=requests.get(ud.name_url,params=test_data)
        assert resp.status_code==200,'HTTP返回码不等于200'
        assert resp.json().get('args').get('name')==test_data.get('name'),'返回名称与传入值不相等'