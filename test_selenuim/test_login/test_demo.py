# !/usr/bin/env Python3
# -*- coding: utf-8 -*-
# @FILE     : test_demo.py
# @Author   : Pluto.
# @Time     : 2020/9/16 13:35
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class TestDemo():
    def setup(self):
        option =Options()
        option.debugger_address = '127.0.0.1:9222'
        self.driver = webdriver.Chrome(options=option)
        # self.driver=webdriver.Chrome()
        self.driver.implicitly_wait(15)

    def teardown(self):
        self.driver.quit()

    def test_demo1(self):
        # self.driver.get("https://ceshiren.com")
        # self.driver.set_window_size(1536,960)
        self.driver.find_element_by_link_text("所有分类").click()
        categoryele = self.driver.find_element_by_link_text("所有分类")
        print(categoryele.get_attribute("class"))
        assert "active" == categoryele.get_attribute("class")