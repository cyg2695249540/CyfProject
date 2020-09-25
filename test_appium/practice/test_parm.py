# !/usr/bin/env Python3
# -*- coding: utf-8 -*-
# @FILE     : test_parm.py
# @Author   : Pluto.
# @Time     : 2020/9/23 20:54
import pytest
from appium import webdriver
from hamcrest import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestParm():
    def setup(self):
        desired_caps = {}
        desired_caps["platformName"] = "Android"
        desired_caps["platformVersion"] = "6.0"
        desired_caps["deviceName"] = "127.0.0.1:7555"
        desired_caps["appPackage"] = "com.xueqiu.android"
        desired_caps["appActivity"] = ".main.view.MainActivity"
        # 不清除数据
        desired_caps["noReset"] = True
        # 不重启应用
        desired_caps["dontStopAppOnReset"] = True
        # 跳过安装，权限设置等操作
        desired_caps["skipDeviceInitialization"] = True
        # 设置可输入中文
        desired_caps["unicodekeyBoard"] = True
        desired_caps["resetkeyBoard"] = True
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.find_element_by_id("com.xueqiu.android:id/action_close").click()

    @pytest.mark.parametrize('searchkey,type,expect_price', [
        ('alibaba', 'BABA', 270),
        ('xiaomi', '01810', 20)
    ])
    def test_parm(self, searchkey, type, expect_price):
        self.driver.find_element_by_id("com.xueqiu.android:id/home_search").click()
        self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys(searchkey)
        self.driver.find_element_by_id("com.xueqiu.android:id/name").click()
        _locator = (By.XPATH, f"//*[@text='{type}']/../../..//*[@resource-id='com.xueqiu.android:id/current_price']")
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(_locator))
        ele = self.driver.find_element(*_locator)
        current_price = float(ele.text)
        print(f"当前的价格为{current_price}")
        assert_that(current_price, close_to(expect_price, expect_price * 0.1))
