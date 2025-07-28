# -*- coding: utf-8 -*-
"""
-------------------------------------------------
# @Project  :pydemo
# @File     :retrytest
# @Date     :2025/6/23 16:18
# @Author   :zhuzhenzhong
# @Description :allure与重试报告信息结合展示失败重试的信息
参考：https://blog.csdn.net/qq_53071851/article/details/131013824?utm_medium=distribute.pc_relevant.none-task-blog-2~default~baidujs_baidulandingword~default-1-131013824-blog-140439688.235^v43^pc_blog_bottom_relevance_base9&spm=1001.2101.3001.4242.2&utm_relevant_index=3
-------------------------------------------------
"""
import os

import allure
import random
import time
import pytest


@allure.step
def passing_step():
    pass


@allure.step
def flaky_broken_step():
    if random.randint(1, 5) != 1:
        raise Exception('Broken!')



@pytest.mark.flaky(reruns=3, reruns_delay=1)  # 如果失败则延迟1s后重试
def test_broken_with_randomized_time():
    passing_step()
    time.sleep(random.randint(1, 3))
    flaky_broken_step()


if __name__ == '__main__':
    pytest.main(['-s', '-q', 'retrytest.py', '--clean-alluredir', '--alluredir=allure-results'])
    # os.system("ls -l")
    os.system(r"allure generate -c -o allure-report")

