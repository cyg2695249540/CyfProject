# !/usr/bin/env Python3
# -*- coding: utf-8 -*-
# @FILE     : test_calc.py
# @Author   : Pluto.
# @Time     : 2020/9/11 11:00
"""
    文件名以test_开头，类以Test开头，方法名以test_开头
    测试类里一定不能加__init__()方法
"""
import pytest
import yaml

from pythoncode.calc import Calculator

with open("./datas/calc.yml") as f:
    datas = yaml.safe_load(f)["add"]
    adddatas = datas["datas"]
    myid = datas["ids"]

class TestCalc():
    def setup_class(self):
        print("开始计算")
        # 实例化计算器
        self.calc = Calculator()

    def teardown_class(self):
        print("结束计算")

    @pytest.mark.add
    def test_fun(self):
        # # 实例化计算器
        # calc = Calculator()
        # 调用它的相加方法
        result = self.calc.add(1, 1)
        # 断言
        assert 2 == result

    @pytest.mark.add
    @pytest.mark.parametrize("a,b,expect", adddatas, ids=myid)
    def test_add(self, a, b, expect):
        # # 实例化计算器
        # calc = Calculator()
        # 调用它的相加方法
        result = self.calc.add(a, b)
        # 如果结果是浮点数,四舍五入取两位
        if isinstance(result, float):
            result = round(result, 2)
        # 断言
        assert expect == result

    @pytest.mark.add
    def test_add1(self):
        # # 实例化计算器
        # calc = Calculator()
        # 调用它的相加方法
        result = self.calc.add(100, 100)
        # 断言
        assert 200 == result

    @pytest.mark.add
    def test_add2(self):
        # # 实例化计算器
        # calc = Calculator()
        # 调用它的相加方法
        result = self.calc.add(-1, -1)
        # 断言
        assert -2 == result

    @pytest.mark.div
    def test_div(self):
        # calc = Calculator()
        result = self.calc.div(1, 1)
        assert 1 == result

    @pytest.mark.div
    def test_div1(self):
        # calc = Calculator()
        result = self.calc.div(-1, 1)
        assert -1 == result
