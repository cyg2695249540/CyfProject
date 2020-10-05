# !/usr/bin/env Python3
# -*- coding: utf-8 -*-
# @FILE     : test_department.py
# @Author   : Pluto.
# @Time     : 2020/9/29 13:47
import json

import yaml
from jsonschema import validate

from test_requests.api.department import Department


class TestDepartment():
    def setup_class(self):
        self.department = Department()
        config_info = yaml.safe_load(open("config.yaml"))
        # 通过传入不同的secret获取不同的token权限给不同的业务测试用例使用
        self.department.get_token(config_info["token"]["department_secret"])

    def test_create_department(self):
        r = self.department.create_department(4)
        assert r["errmsg"] == "created"
        list = self.department.get_department_list()
        assert "技术部" in self.department.base_jsonpath(list, "$..name")

    def test_update_department(self):
        r = self.department.update_department(4)
        assert r["errmsg"] == "updated"
        list = self.department.get_department_list()
        assert "测试研发中心" in self.department.base_jsonpath(list, "$..name")

    def test_delete_department(self):
        self.department.delete_department(4)
        list = self.department.get_department_list()
        assert 4 not in self.department.base_jsonpath(list, "$..id")

    def test_get_department_list(self):
        r = self.department.get_department_list()
        get_list_schema = json.load(open("./json_schema/get_list_schema.json"))
        self.department.base_jsonschema(r, get_list_schema)
