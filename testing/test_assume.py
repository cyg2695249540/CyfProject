# !/usr/bin/env Python3
# -*- coding: utf-8 -*-
# @FILE     : test_assume.py
# @Author   : Pluto.
# @Time     : 2020/9/11 20:40
import pytest


def test_a():
    pytest.assume(1 == 1)
    pytest.assume(False == True)
    pytest.assume(100 == 200)
