# !/usr/bin/env Python3
# -*- coding: utf-8 -*-
# @FILE     : main_page.py
# @Author   : Pluto.
# @Time     : 2020/9/26 11:17
"""
主页:
通讯录
工作台
"""
from appium.webdriver.common.mobileby import MobileBy

from test_appium.page.addresslist_page import AddresslistPage
from test_appium.page.base_page import BasePage


class MainPage(BasePage):
    _addresslist_element = (MobileBy.XPATH,
                           "//*[@resource-id='com.tencent.wework:id/ec6' and @text='通讯录']")
    def goto_addresslist(self):
        # 进入通讯录
        self.find_and_click(self._addresslist_element)
        return AddresslistPage(self.driver)

    def goto_workbench(self):
        pass
