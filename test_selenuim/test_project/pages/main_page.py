# !/usr/bin/env Python3
# -*- coding: utf-8 -*-
# @FILE     : main_page.py
# @Author   : Pluto.
# @Time     : 2020/9/16 21:48
from time import sleep

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

from test_selenuim.test_project.pages.add_member_page import AddMemberPage
from test_selenuim.test_project.pages.basepage import BasePage
from test_selenuim.test_project.pages.contact_page import ContactPage
from selenium import webdriver


class MainPage(BasePage):
    _base_url = "https://work.weixin.qq.com/wework_admin/frame"
    _add_member = (By.XPATH, "//div[@class='index_service']//a[1]")
    _menu_contacts = (By.XPATH, "//header//a[2]//span[1]")

    def go_to_add_member(self):
        # option = Options()
        # option.debugger_address = "127.0.0.1:9222"
        # self.driver = webdriver.Chrome(options=option)
        # self.driver = webdriver.Chrome()
        # self.driver.maximize_window()
        # self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        self.find(*self._add_member).click()
        return AddMemberPage(self.driver)

    def go_to_contact(self):
        self.find(*self._menu_contacts).click()
        return ContactPage(self.driver)
