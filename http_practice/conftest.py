# !/usr/bin/env Python3
# -*- coding: utf-8 -*-
# @FILE     : conftest.py
# @Author   : Pluto.
# @Time     : 2020/9/18 15:55

def pytest_collection_modifyitems(items) -> None:
    for item in items:
        item.name = item.name.encode('utf-8').decode('unicode-escape')
        item._nodeid = item.nodeid.encode('utf-8').decode('unicode-escape')
