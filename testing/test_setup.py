# !/usr/bin/env Python3
# -*- coding: utf-8 -*-
# @FILE     : test_setup.py
# @Author   : Pluto.
# @Time     : 2020/9/11 14:04

def setup_module():
    print("模块级别的setup")

def teardowm_module():
    print("模块级别的teardown")

def setup_function():
    print("函数级别的setup")


def setdown_function():
    print("函数级别的down")


def test_fun():
    print("测试 fun")


class TestDemo:
    def setup_class(self):
        print("类级别的setup")

    def teardown_class(self):
        print("方法级别的teardown")

    def setup(self):
        print("方法级别的setup")

    def teardown(self):
        print("类级别的teardown")

    def test_demo1(self):
        print("test_demo1")

    def test_demo2(self):
        print("test_demo2")

class TestDemo1:
    def setup_class(self):
        print("类级别的setup")

    def teardown_class(self):
        print("类级别的teardown")

    def setup(self):
        print("类里的setup")

    def teardown(self):
        print("类里的teardown")

    def test_demo1(self):
        print("test_demo1")

    def test_demo2(self):
        print("test_demo2")
