# !/usr/bin/env Python3
# -*- coding: utf-8 -*-
# @FILE     : test_demo.py
# @Author   : Pluto.
# @Time     : 2020/9/10 19:07
import yaml
import pytest
class TestDemo():
    @pytest.mark.parametrize("env",yaml.safe_load(open("env.yml")))
    def test_dem0(self,env):
        if "test" in env:
            print("这是测试环境")
            print("测试环境的ip是",env["test"])
        elif "dev" in env:
            print("这是开发环境")
            print("开发环境的ip是", env["dev"])

