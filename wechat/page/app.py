# !/usr/bin/env Python3
# -*- coding: utf-8 -*-
# @FILE     : app.py
# @Author   : Pluto.
# @Time     : 2020/9/26 15:17
from appium import webdriver

from wechat.page.main_page import MainPage


class App():
    def start(self):
        caps = {}
        caps["platformName"] = "Android"
        caps["platformVersion"] = "6.0"
        caps["deviceName"] = "127.0.0.1:7555"
        caps["appPackage"] = "com.tencent.wework"
        caps["appActivity"] = ".launch.WwMainActivity"
        # 不清除数据
        caps["noReset"] = True
        # 不重启应用
        caps["dontStopAppOnReset"] = True
        caps['settings[waitForIdleTimeout]'] = 1  # 等待页面空闲的时间
        # 跳过安装，权限设置等操作
        caps["skipDeviceInitialization"] = True
        # 设置可输入中文
        caps["unicodekeyBoard"] = True
        caps["resetkeyBoard"] = True
        # 自动判断弹框
        caps["autoGrantPermissions"] = True
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(5)

        return self
    def stop(self):
        pass
    def restart(self):
        pass
    def goto_main(self):
        return MainPage()