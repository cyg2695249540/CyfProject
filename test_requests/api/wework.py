# !/usr/bin/env Python3
# -*- coding: utf-8 -*-
# @FILE     : wework.py
# @Author   : Pluto.
# @Time     : 2020/9/29 13:38
import requests

from test_requests.api.base_api import BaseApi


class WeWork(BaseApi):
    def get_token(self,corpsecret):
        # 定义token凭证
        corpid = "ww0ae123b953d2b956"
        # corpsecret = "6EnVDtGal3C_RTpEnNbqr4ynHc7AZ--O3MJg-d7E0Bo"
        # 定义参数
        params = {
            "corpid": corpid,
            "corpsecret": corpsecret
        }
        req = {
            "method": "get",
            "url": f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corpid}&corpsecret={corpsecret}",
                   "params":params
        }
        r = self.send_requests(req)
        self.token = r.json()["access_token"]
        return self.token
