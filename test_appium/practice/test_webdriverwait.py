# !/usr/bin/env Python3
# -*- coding: utf-8 -*-
# @FILE     : test_webdriverwait.py
# @Author   : Pluto.
# @Time     : 2020/9/23 19:17
from appium import webdriver
from hamcrest import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestWebDriverWait():
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
        pass

    def test_wait(self):
        self.driver.find_element_by_id("com.xueqiu.android:id/home_search").click()
        self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys("alibaba")
        self.driver.find_element_by_xpath("//*[@text='阿里巴巴']").click()
        self.driver.find_element_by_xpath("//*[contains(@resource-id,'title_container')]//*[@text='股票']").click()
        _locator = (By.XPATH, "//*[@text='09988']/../../..//*[@resource-id='com.xueqiu.android:id/current_price']")
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(_locator))
        ele = self.driver.find_element(*_locator)
        print(ele)
        current_price = float(ele.text)
        expect_price = 200
        assert_that(current_price, close_to(expect_price, 100))
