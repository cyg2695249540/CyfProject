# !/usr/bin/env Python3
# -*- coding: utf-8 -*-
# @FILE     : test_weixin.py
# @Author   : Pluto.
# @Time     : 2020/9/16 16:51
import shelve
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class TestDemo():
    def setup(self):
        # option = Options()
        # option.debugger_address = '127.0.0.1:9222'
        # self.driver = webdriver.Chrome(options=option)
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_cookie(self):
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        # cookies = self.driver.get_cookies()
        # print(cookies)
        cookies = [
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.d2st', 'path': '/', 'secure': False,
             'value': 'a9148367'},
            {'domain': '.qq.com', 'expiry': 2230974435, 'httpOnly': False, 'name': '_gat', 'path': '/', 'secure': True,
             'value': '1'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/', 'secure': False,
             'value': '1688851206530025'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid', 'path': '/', 'secure': False,
             'value': '1970324964157309'},
            {'domain': '.qq.com', 'expiry': 1663326573, 'httpOnly': False, 'name': '_ga', 'path': '/', 'secure': False,
             'value': 'GA1.2.1695920304.1600253078'},
            {'domain': '.work.weixin.qq.com', 'expiry': 2230974435, 'httpOnly': True, 'name': 'wwrtx.vst', 'path': '/',
             'secure': True,
             'value': 'DbJM8Wa7X_IZ78_D1pXLosHVzuLlRn_J6bCkD6oSwc_h_Zha5od9QqN6_8P5-y03nXH6O1kk1IZuW5MtDyIuuavBSF-B1pk0fIUPKGi0l4_PIcfvjc67IKPwczwa086n0liRMBpTzdAl2W2H6ljC-y8oIDBHsnY_kE1UL64jqQ5RKvAPzLfZoaNfjYRf_oivtEf9vTyWHQhPRUNkNaYe6vMjbrDJT9I9S0yaLO7Dxx5uOurOco2KTJFWCUrasnKIeoJa-SVBaw7HBtAZTwgu4g'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype', 'path': '/', 'secure': False,
             'value': '1'},
            {'domain': '.qq.com', 'expiry': 1600340973, 'httpOnly': False, 'name': '_gid', 'path': '/', 'secure': False,
             'value': 'GA1.2.353240893.1600253078'},
            {'domain': '.work.weixin.qq.com', 'expiry': 2230974435, 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/',
             'secure': True, 'value': 'sites'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid', 'path': '/', 'secure': False,
             'value': '1688851206530025'},
            {'domain': 'work.weixin.qq.com', 'expiry': 2230974435, 'httpOnly': True, 'name': 'ww_rtkey', 'path': '/',
             'secure': True, 'value': '43b3gcp'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/', 'secure': False,
             'value': 'eDFCKFCe06cak8OFW0Dwq0Rhs12hsN_KAUllJv8C9v2Rqqc46Di6Z13hFFsdX-Aw'},
            {'domain': '.work.weixin.qq.com', 'expiry': 2230974435, 'httpOnly': False, 'name': 'wwrtx.c_gdpr',
             'path': '/', 'secure': True, 'value': '0'},
            {'domain': '.work.weixin.qq.com', 'expiry': 2230974435, 'httpOnly': True, 'name': 'wwrtx.refid',
             'path': '/', 'secure': True, 'value': '29352789632675821'},
            {'domain': '.work.weixin.qq.com', 'expiry': 1602846601.064783, 'httpOnly': False, 'name': 'wwrtx.i18n_lan',
             'path': '/', 'secure': False, 'value': 'zh-cn'}]

        for cookie in cookies:
            if 'expiry' in cookie.keys():
                cookie.pop("expiry")
            self.driver.add_cookie(cookie)

        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        sleep(5)

    def test_importcontact(self):
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        # cookies = self.driver.get_cookies()
        cookies = [
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.d2st', 'path': '/', 'secure': False,
             'value': 'a9148367'},
            {'domain': '.qq.com', 'expiry': 2230974435, 'httpOnly': False, 'name': '_gat', 'path': '/', 'secure': True,
             'value': '1'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/', 'secure': False,
             'value': '1688851206530025'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid', 'path': '/', 'secure': False,
             'value': '1970324964157309'},
            {'domain': '.qq.com', 'expiry': 1663326573, 'httpOnly': False, 'name': '_ga', 'path': '/', 'secure': False,
             'value': 'GA1.2.1695920304.1600253078'},
            {'domain': '.work.weixin.qq.com', 'expiry': 2230974435, 'httpOnly': True, 'name': 'wwrtx.vst', 'path': '/',
             'secure': True,
             'value': 'DbJM8Wa7X_IZ78_D1pXLosHVzuLlRn_J6bCkD6oSwc_h_Zha5od9QqN6_8P5-y03nXH6O1kk1IZuW5MtDyIuuavBSF-B1pk0fIUPKGi0l4_PIcfvjc67IKPwczwa086n0liRMBpTzdAl2W2H6ljC-y8oIDBHsnY_kE1UL64jqQ5RKvAPzLfZoaNfjYRf_oivtEf9vTyWHQhPRUNkNaYe6vMjbrDJT9I9S0yaLO7Dxx5uOurOco2KTJFWCUrasnKIeoJa-SVBaw7HBtAZTwgu4g'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype', 'path': '/', 'secure': False,
             'value': '1'},
            {'domain': '.qq.com', 'expiry': 1600340973, 'httpOnly': False, 'name': '_gid', 'path': '/', 'secure': False,
             'value': 'GA1.2.353240893.1600253078'},
            {'domain': '.work.weixin.qq.com', 'expiry': 2230974435, 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/',
             'secure': True, 'value': 'sites'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid', 'path': '/', 'secure': False,
             'value': '1688851206530025'},
            {'domain': 'work.weixin.qq.com', 'expiry': 2230974435, 'httpOnly': True, 'name': 'ww_rtkey', 'path': '/',
             'secure': True, 'value': '43b3gcp'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/', 'secure': False,
             'value': 'eDFCKFCe06cak8OFW0Dwq0Rhs12hsN_KAUllJv8C9v2Rqqc46Di6Z13hFFsdX-Aw'},
            {'domain': '.work.weixin.qq.com', 'expiry': 2230974435, 'httpOnly': False, 'name': 'wwrtx.c_gdpr',
             'path': '/', 'secure': True, 'value': '0'},
            {'domain': '.work.weixin.qq.com', 'expiry': 2230974435, 'httpOnly': True, 'name': 'wwrtx.refid',
             'path': '/', 'secure': True, 'value': '29352789632675821'},
            {'domain': '.work.weixin.qq.com', 'expiry': 1602846601.064783, 'httpOnly': False, 'name': 'wwrtx.i18n_lan',
             'path': '/', 'secure': False, 'value': 'zh-cn'}]

        for cookie in cookies:
            if 'expiry' in cookie.keys():
                cookie.pop("expiry")
            self.driver.add_cookie(cookie)

        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        self.driver.find_element_by_xpath("//div[@class='index_service']//a[2]").click()
        self.driver.find_element_by_xpath("//input[@class='ww_fileImporter_fileContainer_uploadInputMask']").send_keys(
            "C:/Users/uiui/Desktop/txl.xlsx")
        assert "txl.xlsx" == self.driver.find_element_by_xpath(
            "//div[@class='ww_fileImporter_fileContainer_fileNames']").text
        sleep(10)

    def test_shelve(self):
        db = shelve.open("./mydbs/cookies")
        cookies=db["cookie"]
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        for cookie in cookies:
            if 'expiry' in cookie.keys():
                cookie.pop("expiry")
            self.driver.add_cookie(cookie)
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        self.driver.find_element_by_xpath("//div[@class='index_service']//a[2]").click()
        self.driver.find_element_by_xpath("//input[@class='ww_fileImporter_fileContainer_uploadInputMask']").send_keys(
            "C:/Users/uiui/Desktop/txl.xlsx")
        assert "txl.xlsx" == self.driver.find_element_by_xpath(
            "//div[@class='ww_fileImporter_fileContainer_fileNames']").text
        sleep(10)