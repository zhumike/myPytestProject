# -*- coding: utf-8 -*-
'''
@Author : zhuzhenzhong
@File : demotest.py
'''
import httpx
import pytest_check as check

def test_demo():
    for i  in range(3):
        check.equal(i,3,str(i)+" "+"failed")

def test_httpx_get_with_helpers():
    r = httpx.get('https://www.example.org/')
    assert r.status_code == 200
    check.is_false(r.is_redirect)
    check.equal(r.encoding, 'utf-8')
    check.is_in('Example Domain', r.text)