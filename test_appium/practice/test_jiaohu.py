# !/usr/bin/env Python3
# -*- coding: utf-8 -*-
# @FILE     : test_jiaohu.py
# @Author   : Pluto.
# @Time     : 2020/9/24 18:37
from time import sleep

from appium import webdriver
from appium.webdriver.extensions.android.gsm import GsmCallActions


class TestJiaoHu():
    def setup(self):
        desired_caps = {}
        desired_caps["platformName"] = "Android"
        desired_caps["platformVersion"] = "6.0"
        desired_caps["deviceName"] = "emulator-5554"
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

    def teardowm(self):
        self.driver.quit()

    def test_mobile(self):
        # 录屏
        self.driver.start_recording_screen()
        #来电
        self.driver.make_gsm_call("13735825588",GsmCallActions.CALL)
        #短信
        self.driver.send_sms("13967121788","hello appuim api")
        #断网
        self.driver.set_network_connection(1)
        sleep(3)
        self.driver.set_network_connection(4)
        sleep(3)
        #截图
        self.driver.get_screenshot_as_file("./photos/img.png")
        #结束录屏
        self.driver.stop_recording_screen()
