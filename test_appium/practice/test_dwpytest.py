# !/usr/bin/env Python3
# -*- coding: utf-8 -*-
# @FILE     : test_dwpytest.py
# @Author   : Pluto.
# @Time     : 2020/9/23 13:42
import pytest
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction


class TestDW():
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
        self.driver.quit()

    def test_search(self):
        print("搜索测试用例")
        """
        打开雪球APP
        点击搜索输入框
        像搜索输入框里输入”阿里巴巴“
        在搜索结果里选择阿里巴巴，然后点击
        获取这只上 阿里巴巴的股价并判断这只股价的价格>200
        """
        self.driver.find_element_by_id("com.xueqiu.android:id/home_search").click()
        self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys("阿里巴巴")
        self.driver.find_element_by_xpath(
            "//*[@resource-id='com.xueqiu.android:id/name' and @text='阿里巴巴']").click()
        current_price = float(self.driver.find_element_by_id("com.xueqiu.android:id/current_price").text)
        print(current_price)
        assert current_price > 200

    def test_attr(self):
        """
        打开雪球应用首页
        定位首页搜索框
        判断搜索框是否可用，并查看搜索框name属性值
        打印搜索框这个元素左上角坐标和它的高度
        向输入框输入alibaba
        判断阿里巴巴是否可见
        如果可见，打印搜索成功，如果不可见，打印搜索失败
        """
        element = self.driver.find_element_by_id("com.xueqiu.android:id/home_search")
        search_enable = element.is_enabled()
        print(element.text)
        print(element.location)
        print(element.size)
        if search_enable is True:
            element.click()
            self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys("alibaba")
            alibaba_element = self.driver.find_element_by_xpath(
                "//*[@resource-id='com.xueqiu.android:id/name' and @text='阿里巴巴']")
            # assert alibaba_element.is_displayed() is True
            if alibaba_element.get_attribute("displayed") == "true":
                print("搜索成功")
            else:
                print("搜索失败")

    def test_touchaction(self):
        action = TouchAction(self.driver)
        # 获取像素大小
        window_rect = self.driver.get_window_rect()
        width = window_rect["width"]
        height = window_rect["height"]
        x1 = int(width / 2)
        y_start = int(height * 4 / 5)
        y_end = int(height * 1 / 5)
        # 滑动操作
        action.press(x=x1, y=y_start).wait(200).move_to(x=x1, y=y_end).release().perform()

    def test_myinfo(self):
        """
        点击我的，进入到个人信息页面
        点击登录，进入到登录页面
        输入用户名，输入密码
        点击登录
        """
        #text定位，事宜只出现一个的文本
        # self.driver.find_element_by_android_uiautomator('new UiSelector().text("我的")').click()
        #组合定位
        self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.xueqiu.android:id/tab_name")'
                                                        '.text("我的")').click()
        self.driver.find_element_by_android_uiautomator('new UiSelector().textContains("帐号密码")').click()
        self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.xueqiu.android:id/login_account")')\
            .send_keys("1234")
        self.driver.find_element_by_android_uiautomator(
            'new UiSelector().resourceId("com.xueqiu.android:id/login_password")') \
            .send_keys("1234")
        self.driver.find_element_by_android_uiautomator(
            'new UiSelector().resourceId("com.xueqiu.android:id/button_next")').click()

    def test_scroll_find_element(self):
        self.driver.find_element_by_android_uiautomator(
        'new UiScrollable(new UiSelector().scrollable(true).instance(0)).'
        'scrollIntoView(new UiSelector().text("喜狼狼2020").instance(0));').click()
