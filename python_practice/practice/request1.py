# !/usr/bin/env Python3
# -*- coding: utf-8 -*-
# @FILE     : request1.py
# @Author   : Pluto.
# @Time     : 2020/9/10 13:11
import requests
test_params= "q=漫步人生路"
r =requests.get("https://api.douban.com/v2/music/search",params=test_params)
print(r.status_code)
print(r.headers)
print(r.cookies)
print(r.json())
print()
print(r.text)
