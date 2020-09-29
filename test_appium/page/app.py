# !/usr/bin/env Python3
# -*- coding: utf-8 -*-
# @FILE     : app.py
# @Author   : Pluto.
# @Time     : 2020/9/26 11:11
"""
app.py 存放app一些特有操作
启动app：启动应用，关闭应用，重启应用，进入到首页
"""
from appium import webdriver

from test_appium.page.base_page import BasePage
from test_appium.page.main_page import MainPage


class App(BasePage):
    def startapp(self):
        """
        启动app
        """
        if self.driver==None:
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
            #自动判断弹框
            caps["autoGrantPermissions"] = True
            self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
            self.driver.implicitly_wait(5)
        else:
            #launch_app() 复用caps里设置的appActivity不进行初始化操作
            #self.driver.start_activity(appPackage,appActivity) 可以启动任何应用
            self.driver.launch_app()

        return self

    def stopapp(self):
        self.driver.quit()

    def restart(self):
        self.driver.close_app()
        self.driver.launch_app()

    def goto_main(self)->MainPage:
        """
        跳转到首页
        """
        return MainPage(self.driver)
