# !/usr/bin/env Python3
# -*- coding: utf-8 -*-
# @FILE     : test_dingwei.py
# @Author   : Pluto.
# @Time     : 2020/9/23 12:28
from time import sleep

from appium import webdriver
desired_caps={}
desired_caps["platformName"]="Android"
desired_caps["platformVersion"]="6.0"
desired_caps["deviceName"]="127.0.0.1:7555"
desired_caps["appPackage"]="com.xueqiu.android"
desired_caps["appActivity"]=".main.view.MainActivity"
#不清除数据
desired_caps["noReset"]=True
#不重启应用
desired_caps["dontStopAppOnReset"]=True
#跳过安装，权限设置等操作
desired_caps["skipDeviceInitialization"]=True
driver=webdriver.Remote("http://localhost:4723/wd/hub",desired_caps)
driver.implicitly_wait(5)
driver.find_element_by_id("com.xueqiu.android:id/home_search").click()
driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys("alibaba")
driver.back()
driver.back()
driver.find_element_by_accessibility_id()