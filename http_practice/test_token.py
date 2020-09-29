# !/usr/bin/env Python3
# -*- coding: utf-8 -*-
# @FILE     : test_token.py
# @Author   : Pluto.
# @Time     : 2020/9/28 19:39
import requests


class TestToken():
    def test_get_token(self):
        """
        获取 access_token
        """
        # 定义凭证
        _corpid = "ww0ae123b953d2b956"
        _corpsecret = "6EnVDtGal3C_RTpEnNbqr302hRKSkzYRJNQ3o3Ih7CU"
        _url = f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={_corpid}&corpsecret={_corpsecret}"
        # 发送get请求
        r = requests.get(url=_url)
        #打印响应数据
        print(r.json())

    def test_token_param(self):
        """
        获取token第二种形式
        """
        # 定义凭证
        _corpid = "ww0ae123b953d2b956"
        _corpsecret = "6EnVDtGal3C_RTpEnNbqr302hRKSkzYRJNQ3o3Ih7CU"
        _url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken"
        #定义参数
        _params={
            "corpid":_corpid,
            "corpsecret":_corpsecret
        }
        # 发送get请求
        r = requests.get(url=_url,params=_params)
        # 打印响应数据
        print(r.json())




