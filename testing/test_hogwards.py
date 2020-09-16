# !/usr/bin/env Python3
# -*- coding: utf-8 -*-
# @FILE     : test_hogwards.py
# @Author   : Pluto.
# @Time     : 2020/9/15 15:48
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from testing.base import Base


class TestWindow(Base):
    def test_window(self):
        self.driver.get("https://www.baidu.com")
        self.driver.find_element_by_link_text("登录").click()
        print(self.driver.current_window_handle)
        print(self.driver.window_handles)
        self.driver.find_element_by_link_text("立即注册").click()
        print(self.driver.current_window_handle)
        print(self.driver.window_handles)
        windows =self.driver.window_handles
        self.driver.switch_to_window(windows[-1])
        self.driver.find_element_by_xpath("//input[@id='TANGRAM__PSP_4__userName']").send_keys("username")
        sleep(2)
        self.driver.switch_to_window(windows[0])
        self.driver.find_element_by_xpath("//p[@id='TANGRAM__PSP_11__footerULoginBtn']").click()
        self.driver.find_element_by_xpath("//input[@id='TANGRAM__PSP_11__userName']").send_keys("username")
        self.driver.find_element_by_xpath("//input[@id='TANGRAM__PSP_11__submit']").click()
        sleep(3)
