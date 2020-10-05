# !/usr/bin/env Python3
# -*- coding: utf-8 -*-
# @FILE     : base_api.py
# @Author   : Pluto.
# @Time     : 2020/9/29 15:29
import requests
from jsonpath import jsonpath
from jsonschema import validate


class BaseApi():
    def send_requests(self,req:dict):
        """
        对requests进行二次封装
        """
        #不定长关键字传参
        #字典解包进行关键字传参
        return requests.request(**req)

    def base_jsonpath(self,obj,json_expr):
        return jsonpath(obj,json_expr)

    def base_jsonschema(self,instance,schema):
        return validate(instance,schema)