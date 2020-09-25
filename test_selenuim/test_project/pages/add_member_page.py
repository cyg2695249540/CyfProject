# !/usr/bin/env Python3
# -*- coding: utf-8 -*-
# @FILE     : add_member_page.py
# @Author   : Pluto.
# @Time     : 2020/9/16 21:49
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

from test_selenuim.test_project.pages.basepage import BasePage
from test_selenuim.test_project.pages.contact_page import ContactPage


class AddMemberPage(BasePage):
    def add_member(self,username,acctid,memberAdd_phone):
        # option = Options()
        # option.debugger_address = "127.0.0.1:9222"
        # self.driver = webdriver.Chrome(options=option)
        # self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.find(By.XPATH,"//input[@id='username']").send_keys(username)
        self.find(By.XPATH,"//input[@id='memberAdd_acctid']").send_keys(acctid)
        self.find(By.XPATH,"//input[@id='memberAdd_phone']").send_keys(memberAdd_phone)
        return self

    def save_member(self):
        self.find(By.XPATH,"//div[@class='member_edit']//div[1]//a[2]").click()
        return ContactPage(self.driver)

    def cancel_member(self):
        self.find(By.XPATH,"//div[contains(@class,'member_edit')]//div[1]//a[3]").click()
        self.find(By.CSS_SELECTOR,"[node-type='cancel']").click()
        return ContactPage(self.driver)
