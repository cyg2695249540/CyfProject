# !/usr/bin/env Python3
# -*- coding: utf-8 -*-
# @FILE     : test_rerun.py
# @Author   : Pluto.
# @Time     : 2020/9/11 19:46
import pytest


def test_rerun1():
    assert 1 == 2


def test_rerun2():
    assert 2 == 2


@pytest.mark.flaky(reruns=5, reruns_delay=2)
def test_rerun3():
    assert 3 == 2
