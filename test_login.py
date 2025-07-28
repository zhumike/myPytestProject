# -*- coding: utf-8 -*-
# @Time : 2021/5/31 4:59 下午
# @Author : zhuzhenzhong
import json

import  pytest
import  requests
import  yaml


def readYaml():
   with open('test_yaml_login.yml','r') as f:
      return list(yaml.safe_load_all(f))


@pytest.mark.parametrize('data',readYaml())
def test_login(data):
   r=requests.post(
      url=data['url'],
      json=json.loads(data['body']))
   assert r.json()==json.loads(data['expect'])
