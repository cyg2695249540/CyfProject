# !/usr/bin/env Python3
# -*- coding: utf-8 -*-
# @FILE     : request2.py
# @Author   : Pluto.
# @Time     : 2020/9/10 13:11
import requests
test_data= {"q" : "漫步人生路"}
r =requests.post("https://api.douban.com/v2/music/search",data=test_data)
print(r.status_code)
print(r.headers)
print(r.cookies)
print(r.json())
print()
print(r.text)