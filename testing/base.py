# !/usr/bin/env Python3
# -*- coding: utf-8 -*-
# @FILE     : base.py
# @Author   : Pluto.
# @Time     : 2020/9/15 19:46
import os

from selenium import webdriver


class Base():
    def setup(self):
        browser = os.getenv("browser")
        if browser == "firefox":
            self.driver = webdriver.Firefox()
        else:
            self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

    def teardown(self):
        self.driver.quit()
