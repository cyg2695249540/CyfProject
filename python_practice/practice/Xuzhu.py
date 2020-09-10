# !/usr/bin/env Python3
# -*- coding: utf-8 -*-
# @FILE     : Xuzhu.py
# @Author   : Pluto.
# @Time     : 2020/9/9 21:45
"""
定义一个XuZhu类，继承于童姥。虚竹宅心仁厚不想打架。所以虚竹只有一个read（念经）的方法。每次调用都会打印“罪过罪过”
"""
from python_practice.practice.Tonglao import TongLao


class XuZhu(TongLao):
    def __init__(self):
        pass
    def read(self):
        print("罪过罪过")

xz = XuZhu()
xz.read()