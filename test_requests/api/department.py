# !/usr/bin/env Python3
# -*- coding: utf-8 -*-
# @FILE     : department.py
# @Author   : Pluto.
# @Time     : 2020/9/29 13:39
import requests

from test_requests.api.wework import WeWork


class Department(WeWork):
    def create_department(self,department_id):
        create_url = f"https://qyapi.weixin.qq.com/cgi-bin/department/create?access_token={self.token}"
        data = {
            "name": "技术部",
            "name_en": "JSB",
            "parentid": 1,
            "order": 1,
            "id": department_id
        }
        # 企业微信接口使用https，json，utf-8
        r = requests.post(url=create_url, json=data)
        return r.json()

    def update_department(self, department_id):
        update_url = f"https://qyapi.weixin.qq.com/cgi-bin/department/update?access_token={self.token}"
        data = {
            "id": department_id,
            "name": "测试研发中心",
            "name_en": "RDGZ",
            "parentid": 1,
            "order": 1
        }
        r = requests.post(url=update_url, json=data)
        return r.json()

    def delete_department(self,department_id):
        delete_url = f"https://qyapi.weixin.qq.com/cgi-bin/department/delete?access_token={self.token}&id={department_id}"
        r = requests.get(url=delete_url)
        return r.json()

    def get_department_list(self):
        get_depement_list_url = f"https://qyapi.weixin.qq.com/cgi-bin/department/list?access_token={self.token}"
        list = requests.get(url=get_depement_list_url)
        return list.json()
