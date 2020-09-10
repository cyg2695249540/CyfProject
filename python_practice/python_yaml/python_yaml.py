# !/usr/bin/env Python3
# -*- coding: utf-8 -*-
# @FILE     : python_yaml.py
# @Author   : Pluto.
# @Time     : 2020/9/10 14:46
import yaml


yaml_data = yaml.safe_load(open("data2.yml",encoding='utf-8'))
print(yaml_data)