# !/usr/bin/env Python3
# -*- coding: utf-8 -*-
# @FILE     : test_order.py
# @Author   : Pluto.
# @Time     : 2020/9/11 20:49
from time import sleep

import pytest


@pytest.mark.run(order=3)
def test_foo():
    sleep(1)
    assert True


@pytest.mark.run(order=2)
def test_bar():
    sleep(1)
    assert True

@pytest.mark.run(order=1)
def test_aar():
    sleep(1)
    assert True
