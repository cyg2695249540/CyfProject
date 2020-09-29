# !/usr/bin/env Python3
# -*- coding: utf-8 -*-
# @FILE     : test_contact.py
# @Author   : Pluto.
# @Time     : 2020/9/26 15:17
from wechat.page.app import App


class TestContact():
    def setup(self):
        self.app=App()
        self.driver=self.app.start().goto_main()
    def teardown(self):
        self.app.stop()
    def test_addcontact(self):
        self.main