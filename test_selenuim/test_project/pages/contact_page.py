# !/usr/bin/env Python3
# -*- coding: utf-8 -*-
# @FILE     : contact_page.py
# @Author   : Pluto.
# @Time     : 2020/9/16 21:48
from time import sleep

from selenium.webdriver.common.by import By

from test_selenuim.test_project.pages.basepage import BasePage


class ContactPage(BasePage):
    _add_member=(By.XPATH,"//body/div/div/div/main/div/div/div/div/div/div[3]/div[1]/a[1]")
    def go_to_add_member(self):
        #解决循环导入问题
        from test_selenuim.test_project.pages.add_member_page import AddMemberPage
        self.wait_for_clickabel(self._add_member)
        self.find(*self._add_member).click()
        return AddMemberPage(self.driver)

    def get_member_list(self):
        sleep(1)
        ele=self.finds(By.CSS_SELECTOR,".member_colRight_memberTable_td:nth-child(2)")
        return [name.text for name in ele]
        # list1=[]
        # print(ele)
        # for name in ele:
        #     list1.append(name.text)