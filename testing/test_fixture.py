# !/usr/bin/env Python3
# -*- coding: utf-8 -*-
# @FILE     : test_fixture.py
# @Author   : Pluto.
# @Time     : 2020/9/11 18:24
import pytest

# 创建一个登陆的fixture方法,yield关键字激活fixture的teardown方法
@pytest.fixture()
def login():
    print("登陆操作")
    print("获取token")
    yield
    print("登出操作")

# 需要提前登陆
# 在执行测试用例之前会执行传入的login方法
def test_case1(login):
    print("测试用例1")
# 不需要提前登陆
def test_case2():
    print("测试用例2")
# 需要提前登陆
def test_case3(login):
    print("测试用例3")