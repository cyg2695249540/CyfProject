# !/usr/bin/env Python3
# -*- coding: utf-8 -*-
# @FILE     : test_a.py
# @Author   : Pluto.
# @Time     : 2020/9/10 18:09
import pytest
import yaml


def inc(x):
    return x + 1

@pytest.mark.parametrize(("a,b"), yaml.safe_load(open("test_a.yml")))
def test_answer1(a,b):
    assert inc(a) == b
def test_answer2():
    assert inc(4) == 5
@pytest.fixture()
def login():
    print("登录操作")
    username = "Pluto."
    return  username
class TestDemo():
    def test_a(self,login):
        print(f"a username = {login}")
    def test_b(self):
        print("b")
    def test_c(self,login):
        print(f"c username = {login}")

