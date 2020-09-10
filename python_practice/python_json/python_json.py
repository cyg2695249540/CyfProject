# !/usr/bin/env Python3
# -*- coding: utf-8 -*-
# @FILE     : python_json.py
# @Author   : Pluto.
# @Time     : 2020/9/10 14:29
import json
dict_hh = {
    "a" : [1,2,3],
    "name" : ["sprider man","星矢"]
}
# 在data.json中写入数据
with open("data.json","w") as f:
    json.dump(dict_hh,f,ensure_ascii=False)
