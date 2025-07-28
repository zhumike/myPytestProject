# -*- coding: utf-8 -*-
# @Time : 2021/6/22 6:00 下午
# @Author : zhuzhenzhong
import os
import pytest
import yaml

@pytest.fixture(scope="session")
def env(request):
    config_path = os.path.join(request.config.rootdir,
                               "config",
                               "test",
                               "config.yaml")
    with open(config_path) as f:
        env_config = yaml.load(f.read(), Loader=yaml.SafeLoader)
    return env_config