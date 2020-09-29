# !/usr/bin/env Python3
# -*- coding: utf-8 -*-
# @FILE     : addresslist_page.py
# @Author   : Pluto.
# @Time     : 2020/9/26 11:21
"""
通讯录页面
"""
from appium.webdriver.common.mobileby import MobileBy

from test_appium.page.base_page import BasePage
from test_appium.page.member_invite_page import MemberInvitePage


class AddresslistPage(BasePage):
    _addmemeber_text="添加成员"
    _search_element=(MobileBy.ID, "com.tencent.wework:id/hxw")
    def add_memeber(self):
        self.find_by_scroll_and_click(self._addmemeber_text)
        return MemberInvitePage(self.driver)
    def search(self):
        pass
