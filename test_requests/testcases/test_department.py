# !/usr/bin/env Python3
# -*- coding: utf-8 -*-
# @FILE     : test_department.py
# @Author   : Pluto.
# @Time     : 2020/9/29 13:47
from test_requests.api.department import Department

class TestDepement():
    def setup_class(self):
        self.depement = Department()
        self.depement.get_token()

    def test_create_department(self):
        r = self.depement.create_department(4)
        assert r["errmsg"] == "created"
        list = self.depement.get_department_list()
        assert list["department"][3]["name"] == "技术部"

    def test_update_department(self):
        r = self.depement.update_department(4)
        assert r["errmsg"] == "updated"
        list = self.depement.get_department_list()
        assert list["department"][3]["name"] == "测试研发中心"

    def test_delete_department(self):
        self.depement.delete_department(4)
        list = self.depement.get_department_list()
        assert len(list["department"]) == 3
