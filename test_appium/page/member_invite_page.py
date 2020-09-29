# !/usr/bin/env Python3
# -*- coding: utf-8 -*-
# @FILE     : member_invite_page.py
# @Author   : Pluto.
# @Time     : 2020/9/26 11:23
"""
添加成员页面
"""
# from test_appium.page.contact_edit_page import ContactEditPage
from appium.webdriver.common.mobileby import MobileBy

from test_appium.page.base_page import BasePage


class MemberInvitePage(BasePage):
    _addmember_element=(MobileBy.XPATH, "//*[@text='手动输入添加']")
    def addcontact_menual(self):
        #点击手动输入添加
        self.find_and_click(self._addmember_element)
        from test_appium.page.contact_edit_page import ContactEditPage
        return ContactEditPage(self.driver)

    def get_toast(self):
        mytoast =self.get_toast_text()
        return mytoast