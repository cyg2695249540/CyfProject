# !/usr/bin/env Python3
# -*- coding: utf-8 -*-
# @FILE     : test1.py
# @Author   : Pluto.
# @Time     : 2020/9/10 11:07
import time
print(time.localtime())
print(time.strftime('%Y{y}%m{m}%d{d} %H{h}%M{f}%S{s}').format(y='年', m='月', d='日', h='时', f='分', s='秒'))