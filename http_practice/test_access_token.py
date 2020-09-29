# !/usr/bin/env Python3
# -*- coding: utf-8 -*-
# @FILE     : test_access_token.py
# @Author   : Pluto.
# @Time     : 2020/9/28 21:56
import pytest
import requests


class TestToken():
    # 正向
    def test_token(self):
        # 定义凭证
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
        # 打印响应数据
        print(r.json())
        assert r.json()["errcode"] == 0 and r.json()["errmsg"] == "ok"

    # [异常]不传id
    def test_token1(self):
        # 定义凭证
        corpid = "ww0ae123b953d2b956"
        corpsecret = "6EnVDtGal3C_RTpEnNbqr4ynHc7AZ--O3MJg-d7E0Bo"
        token_url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken"
        # 定义参数
        params = {
            # "corpid": corpid,
            "corpsecret": corpsecret
        }
        # 发送get请求
        r = requests.get(url=token_url, params=params)
        # 打印响应数据
        print(r.json())
        assert r.json()["errcode"] == 41002 and r.json()["errmsg"] == "corpid missing"

    # [异常]不传secret
    def test_token2(self):
        # 定义凭证
        corpid = "ww0ae123b953d2b956"
        corpsecret = "6EnVDtGal3C_RTpEnNbqr4ynHc7AZ--O3MJg-d7E0Bo"
        token_url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken"
        # 定义参数
        params = {
            "corpid": corpid,
            # "corpsecret": corpsecret
        }
        # 发送get请求
        r = requests.get(url=token_url, params=params)
        # 打印响应数据
        print(r.json())
        assert r.json()["errcode"] == 41004 and r.json()["errmsg"] == "corpsecret missing"

    # 参数化
    @pytest.mark.parametrize(
        "corp_id,corp_secret,errmsg", [("ww0ae123b953d2b956", "6EnVDtGal3C_RTpEnNbqr4ynHc7AZ--O3MJg-d7E0Bo", "ok"),
                                       ("", "6EnVDtGal3C_RTpEnNbqr4ynHc7AZ--O3MJg-d7E0Bo", "corpid missing"),
                                       ("ww0ae123b953d2b956", "", "corpsecret missing")
                                       ], ids=["正向", "[异常]不传id", "[异常]不传secret"])
    def test_token0(self, corp_id, corp_secret, errmsg):
        token_url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken"
        # 定义参数
        params = {
            "corpid": corp_id,
            "corpsecret": corp_secret
        }
        # 发送get请求
        r = requests.get(url=token_url, params=params)
        print(r.json())
        assert r.json()["errmsg"] == errmsg
