# !/usr/bin/env Python3
# -*- coding: utf-8 -*-
# @FILE     : test_departments.py
# @Author   : Pluto.
# @Time     : 2020/9/28 20:01
import requests


class TestDepements():
    def setup(self):
        """
        获取token
        """
        # 定义凭证
        corpid = "ww0ae123b953d2b956"
        corpsecret = "6EnVDtGal3C_RTpEnNbqr30oNHp_vG8Q01EEnqr8xLg"
        url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken"
        # 定义参数
        params = {
            "corpid": corpid,
            "corpsecret": corpsecret
        }
        # 发送get请求
        r = requests.get(url=url, params=params)
        # 获取access_token
        self.token = r.json()["access_token"]

    def teardown(self):
        pass

    def test_create_depements(self):
        """
        创建部门
        """
        url = "https://qyapi.weixin.qq.com/cgi-bin/department/create"
        # 定义请求参数
        param = {
            "access_token": self.token
        }
        # 定义请求体
        data = {
            "name": "技术部",
            "name_en": "LCQ",
            "parentid": 1,
            "order": 3,
            "id": 4
        }
        # 发送post请求
        r = requests.post(url=url, json=data, params=param)
        # 打印响应
        print(r.json())
        assert r.json()["errcode"] == 0 and r.json()["errmsg"] == "created"
