# !/usr/bin/env Python3
# -*- coding: utf-8 -*-
# @FILE     : test_scope.py
# @Author   : Pluto.
# @Time     : 2020/9/11 19:07
import pytest


def test_a(connectDB):
    print("测试用例a")


class TestDemo():
    def test_b(self, connectDB):
        print("测试用例b")

    def test_c(self, connectDB):
        print("测试用例c")
