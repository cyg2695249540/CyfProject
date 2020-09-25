# !/usr/bin/env Python3
# -*- coding: utf-8 -*-
# @FILE     : test_browser.py
# @Author   : Pluto.
# @Time     : 2020/9/24 12:46
from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestBrowser():
    def setup(self):
        desired_caps = {}
        desired_caps["platformName"] = "Android"
        desired_caps["platformVersion"] = "6.0"
        desired_caps["deviceName"] = "127.0.0.1:7555"
        # desired_caps["platformName"] = "Android"
        # desired_caps["platformVersion"] = "6.0"
        # desired_caps["deviceName"] = "emulator-5554"
        desired_caps["browserName"] = "Browser"
        # desired_caps["appPackage"] = "com.android.browser"
        # desired_caps["appActivity"] = ".BrowserActivity"
        # 设置可输入中文
        desired_caps["unicodekeyBoard"] = True
        desired_caps["resetkeyBoard"] = True
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)
        self.driver.implicitly_wait(5)

    def teardown(self):
        # self.driver.quit()
        pass
    def test_browser(self):
        self.driver.get("http://m.baidu.com")
        self.driver.find_element_by_id("index-kw").click()
        self.driver.find_element_by_id("index-kw").send_keys("appium")
        _located=(By.ID,"index-bn")
        WebDriverWait(self.driver,10).until(expected_conditions.visibility_of_element_located(_located))
        self.driver.find_element(*_located).click()
