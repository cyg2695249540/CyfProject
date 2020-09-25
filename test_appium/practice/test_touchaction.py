# !/usr/bin/env Python3
# -*- coding: utf-8 -*-
# @FILE     : test_touchaction.py
# @Author   : Pluto.
# @Time     : 2020/9/23 15:58
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction


class TestTouchAction():
    def setup(self):
        desired_caps = {}
        desired_caps["platformName"] = "Android"
        desired_caps["platformVersion"] = "6.0"
        desired_caps["deviceName"] = "127.0.0.1:7555"
        desired_caps["appPackage"] = "cn.kmob.screenfingermovelock"
        desired_caps["appActivity"] = "com.samsung.ui.FlashActivity"
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
        self.driver.quit()

    def test_touchaction_unlock(self):
        self.driver.find_element_by_id("cn.kmob.screenfingermovelock:id/topLayout").click()
        action = TouchAction(self.driver)
        action.press(x=121, y=187).wait(100).move_to(x=355, y=177).wait(100).move_to(x=604, y=179) \
            .wait(100).move_to(x=602, y=424).wait(100).move_to(x=604, y=664).wait(100).release().perform()
