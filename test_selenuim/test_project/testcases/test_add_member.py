# !/usr/bin/env Python3
# -*- coding: utf-8 -*-
# @FILE     : test_add_member.py
# @Author   : Pluto.
# @Time     : 2020/9/17 14:29
import pytest

from test_selenuim.test_project.pages.main_page import MainPage


class TestAddMember:
    def setup(self):
        self.main = MainPage()

    @pytest.mark.parametrize("username,acctid,memberAdd_phone", [("ez", 55555, 13711111111)], ids={"添加成员"})
    def test_add_member(self, username, acctid, memberAdd_phone):
        namelist = self.main.go_to_add_member().add_member(username, acctid,
                                                           memberAdd_phone).save_member().get_member_list()
        assert username in namelist

    @pytest.mark.parametrize("username,acctid,memberAdd_phone", [("ez3", 55555, 13711111111)], ids={"取消添加成员"})
    def test_add_member_fail(self, username, acctid, memberAdd_phone):
        namelist = self.main.go_to_add_member().add_member(username, acctid,
                                                           memberAdd_phone).cancel_member().get_member_list()
        assert username not in namelist

    @pytest.mark.parametrize("username,acctid,memberAdd_phone", [("ez2", 66666, 13711111112)], ids={"通讯录添加成员"})
    def test_contact_member(self, username, acctid, memberAdd_phone):
        namelist = self.main.go_to_contact().go_to_add_member().add_member(username, acctid, memberAdd_phone).save_member().get_member_list()
        assert username in namelist

    def teardow(self):
        self.main.driver.quit()
