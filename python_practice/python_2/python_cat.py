# !/usr/bin/env Python3
# -*- coding: utf-8 -*-
# @FILE     : python_cat.py
# @Author   : Pluto.
# @Time     : 2020/9/9 18:19
class Cat():
    color = "orange"
    leg = 4
    def eat(self):
        print("猫在吃")
    def cry(self):
        print("猫在叫")


print(Cat.color)
Cat().eat()