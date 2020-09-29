# !/usr/bin/env Python3
# -*- coding: utf-8 -*-
# @FILE     : test_data.py
# @Author   : Pluto.
# @Time     : 2020/9/26 16:42
from selenium import webdriver


class TestData():
    def test_data(self):
        driver=webdriver.Chrome()
        driver.get("https://home.testing-studio.com")
        print(driver.execute_script("return JSON.stringify(window.performance.timing)"))