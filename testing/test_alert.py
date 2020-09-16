# !/usr/bin/env Python3
# -*- coding: utf-8 -*-
# @FILE     : test_alert.py
# @Author   : Pluto.
# @Time     : 2020/9/16 11:16
from time import sleep

from selenium.webdriver import ActionChains

from testing.base import Base


class TestAlert(Base):
    def test_alert(self):
        self.driver.get("https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable")
        self.driver.switch_to.frame("iframeResult")
        drag=self.driver.find_element_by_xpath("//div[@id='draggable']")
        drop=self.driver.find_element_by_xpath("//div[@id='droppable']")
        action=ActionChains(self.driver)
        action.drag_and_drop(drag,drop).perform()
        print("点击alert确认")
        self.driver.switch_to.alert.accept()
        self.driver.switch_to.default_content()
        self.driver.find_element_by_xpath("//button[@id='submitBTN']").click()
        sleep(3)