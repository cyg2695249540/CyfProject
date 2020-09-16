# !/usr/bin/env Python3
# -*- coding: utf-8 -*-
# @FILE     : test_js.py
# @Author   : Pluto.
# @Time     : 2020/9/16 10:49


from testing.base import Base


class TestJs(Base):
    def test_datatime(self):
        self.driver.get("https://www.12306.cn/index/")
