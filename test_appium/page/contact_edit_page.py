# !/usr/bin/env Python3
# -*- coding: utf-8 -*-
# @FILE     : contact_edit_page.py
# @Author   : Pluto.
# @Time     : 2020/9/26 11:37
# from test_appium.page.member_invite_page import MemberInvitePage
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from test_appium.page.base_page import BasePage


class ContactEditPage(BasePage):
    _name_element=(MobileBy.XPATH,
                                 "//*[contains(@text,'姓名')]/..//*[@class='android.widget.EditText']")
    _gender_element=(MobileBy.XPATH, "//*[@text='男']")
    _female_element=(MobileBy.XPATH, "//*[@text='女']")
    _male_element=(MobileBy.XPATH, "//*[@text='男']")
    _phonenum_element=(MobileBy.XPATH,
                                 "//*[contains(@text,'手机') and @class='android.widget.TextView']/..//*[@class='android.widget.EditText']")
    _save_element=(MobileBy.XPATH, "//*[@text='保存']")
    def edit_name(self,_name):
        self.find_and_sendkeys(self._name_element,_name)
        return self

    def edit_gender(self, _gender):
        self.find_and_click(self._gender_element)
        if _gender=="女":
            self.find_and_click(self._female_element)
        else:
            self.find_and_click(self._male_element)

        # if _gender == "女":
        #     _searchtext = (MobileBy.XPATH, "//*[@text='女']")
        #     element = WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(_searchtext))
        #     element.click()
        # else:
        #     element = WebDriverWait(self.driver, 10).until(lambda x: x.find_element(MobileBy.XPATH, "//*[@text='男']"))
        #     element.click()
        return self

    def edit_phonenum(self, _phonenum):
        self.find_and_sendkeys(self._phonenum_element,_phonenum)
        return self

    def click_save(self):
        self.find_and_click(self._save_element)
        from test_appium.page.member_invite_page import MemberInvitePage
        return MemberInvitePage(self.driver)
