# !/usr/bin/env Python3
# -*- coding: utf-8 -*-
# @FILE     : test_frame.py
# @Author   : Pluto.
# @Time     : 2020/9/15 20:46
from testing.base import Base


class TestFrame(Base):
    def testframe(self):
        self.driver.get("https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable")
        self.driver.switch_to.frame("iframeResult")
        print(self.driver.find_element_by_xpath("//div[@id='draggable']").text)
        # self.driver.switch_to.default_content()
        self.driver.switch_to.parent_frame()
        print(self.driver.find_element_by_xpath("//button[@id='submitBTN']").text)