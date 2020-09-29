# !/usr/bin/env Python3
# -*- coding: utf-8 -*-
# @FILE     : wework.py
# @Author   : Pluto.
# @Time     : 2020/9/29 13:38
import requests


class WeWork():
    def get_token(self):
        # 定义token凭证
        corpid = "ww0ae123b953d2b956"
        corpsecret = "6EnVDtGal3C_RTpEnNbqr4ynHc7AZ--O3MJg-d7E0Bo"
        token_url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken"
        # 定义参数
        params = {
            "corpid": corpid,
            "corpsecret": corpsecret
        }
        # 发送get请求
        r = requests.get(url=token_url, params=params)
        self.token =r.json()["access_token"]
        return self.token
