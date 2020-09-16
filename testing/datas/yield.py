# !/usr/bin/env Python3
# -*- coding: utf-8 -*-
# @FILE     : yield.py
# @Author   : Pluto.
# @Time     : 2020/9/11 18:44

def provider():
    for i in range(0, 10):
        print("开始操作")
        yield i  # 相当于return i,并保存当前位置
        print("结束操作")

p = provider()
for i in p:
    print(i)
