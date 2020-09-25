# !/usr/bin/env Python3
# -*- coding: utf-8 -*-
# @FILE     : test_hamrest.py
# @Author   : Pluto.
# @Time     : 2020/9/23 20:44
from hamcrest import *


class TestHamrest():
    def test_hamrest(self):
        # assert_that(10,equal_to(9),"这是一个提示")
        assert_that(8.8,close_to(10,2),"这是一个丢包提示")
        assert_that("contains some string",contains_string("string"))