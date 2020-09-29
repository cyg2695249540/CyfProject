# !/usr/bin/env Python3
# -*- coding: utf-8 -*-
# @FILE     : base_api.py
# @Author   : Pluto.
# @Time     : 2020/9/29 15:29
import requests


class BaseApi():
    def send_requests(self,req:dict):
        """
        对requests进行二次封装
        """
        #字典解包进行关键字传参
        return requests.request(**req)