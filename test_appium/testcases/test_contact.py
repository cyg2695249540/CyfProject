# !/usr/bin/env Python3
# -*- coding: utf-8 -*-
# @FILE     : test_contact.py
# @Author   : Pluto.
# @Time     : 2020/9/26 11:27
from test_appium.page.app import App


class TestContact():
    def setup(self):
        """
        应用启动
        """
        self.app = App()
        self.main = self.app.startapp().goto_main()

    def teardown(self):
        """
        应用关闭
        """
        self.app.stopapp()

    def test_addcontact(self):
        _name="xxx"
        _gender="女"
        _phonenum="13711111116"
        mypage = self.main.goto_addresslist().add_memeber().addcontact_menual() \
            .edit_name(_name).edit_gender(_gender).edit_phonenum(_phonenum).click_save()
        mytost = mypage.get_toast()
        assert mytost == "添加成功"

    def test_delcontact(self):
        pass


