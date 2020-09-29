# !/usr/bin/env Python3
# -*- coding: utf-8 -*-
# @FILE     : test_department_practice.py
# @Author   : Pluto.
# @Time     : 2020/9/29 12:40
import requests
from hamcrest import assert_that
from jsonpath import jsonpath


class TestDepartmentPractice():
    def setup(self):
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
        self.token = r.json()["access_token"]
        self.id = 4

    def test_create_department(self):
        create_url = f"https://qyapi.weixin.qq.com/cgi-bin/department/create?access_token={self.token}"
        data = {
            "name": "技术部",
            "name_en": "JSB",
            "parentid": 1,
            "order": 1,
            "id": self.id
        }
        # 企业微信接口使用https，json，utf-8
        r = requests.post(url=create_url, json=data)
        # print(r.json())
        assert r.json()["errmsg"] == "created"
        get_depement_list_url = f"https://qyapi.weixin.qq.com/cgi-bin/department/list?access_token={self.token}"
        list = requests.get(url=get_depement_list_url)
        # print(list.json())
        assert list.json()["department"][self.id - 1]["name"] == "技术部"
        # assert_that(jsonpath(list.json()),)

    def test_update_department(self):
        update_url = f"https://qyapi.weixin.qq.com/cgi-bin/department/update?access_token={self.token}"
        data = {
            "id": self.id,
            "name": "测试研发中心",
            "name_en": "RDGZ",
            "parentid": 1,
            "order": 1
        }
        r = requests.post(url=update_url, json=data)
        assert r.json()["errmsg"] == "updated"
        # 数据验证
        get_depement_list_url = f"https://qyapi.weixin.qq.com/cgi-bin/department/list?access_token={self.token}"
        list = requests.get(url=get_depement_list_url)
        # print(list.json())
        assert list.json()["department"][self.id - 1]["name"] == "测试研发中心"

    def test_delete_department(self):
        delete_url = f"https://qyapi.weixin.qq.com/cgi-bin/department/delete?access_token={self.token}&id={self.id}"
        r = requests.get(url=delete_url)
        assert r.json()["errmsg"] == "deleted"

        get_depement_list_url = f"https://qyapi.weixin.qq.com/cgi-bin/department/list?access_token={self.token}"
        list = requests.get(url=get_depement_list_url)
        assert len(list.json()["department"]) == self.id - 1
