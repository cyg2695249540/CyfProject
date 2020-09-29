# !/usr/bin/env Python3
# -*- coding: utf-8 -*-
# @FILE     : test_demo.py
# @Author   : Pluto.
# @Time     : 2020/9/28 14:18
import requests
from jsonpath import jsonpath
from hamcrest import assert_that, equal_to
from requests.auth import HTTPBasicAuth


class TestDemo:
    def test_get(self):
        r = requests.get("https://httpbin.testing-studio.com/get")
        print(r.status_code)
        print(r.text)
        print(r.json())
        assert r.status_code == 200

    def test_query(self):
        playload = {
            "level": 1,
            "name": "seveniruby"
        }
        r = requests.get("https://httpbin.testing-studio.com/get", params=playload)
        print(r.text)
        assert r.status_code == 200

    def test_post_form(self):
        playload = {
            "level": 1,
            "name": "seveniruby"
        }
        r = requests.post("https://httpbin.testing-studio.com/post", data=playload)
        print(r.text)
        assert r.status_code == 200

    def test_post_header(self):
        r = requests.get("https://httpbin.testing-studio.com/get", headers={"h": "hello demo"})
        print(r.status_code)
        print(r.text)
        print(r.json())
        assert r.status_code == 200
        assert_that(r.json()["headers"]["H"], equal_to("hello demo"))

    def test_post_json(self):
        json = {
            "level": 1,
            "name": "seveniruby"
        }
        r = requests.post("https://httpbin.testing-studio.com/post", json=json)
        print(r.text)
        assert r.status_code == 200

    def test_hogwarts_json(self):
        r = requests.get("https://home.testing-studio.com/categories.json")
        print(r.text)
        assert r.status_code == 200
        assert r.json()["category_list"]["categories"][0]["name"] == "社区治理"
        print(jsonpath(r.json(), "$..name"))
        assert jsonpath(r.json(), "$..name")[0] == "社区治理"
        assert "社区治理" in jsonpath(r.json(), "$..name")

    def test_hamcrest(self):
        r = requests.get("https://home.testing-studio.com/categories.json")
        print(r.text)
        assert r.status_code == 200
        assert_that(jsonpath(r.json(), "$..name")[0], equal_to("社区治理"))

    def test_cookie(self):
        url = "https://httpbin.testing-studio.com/cookies"
        header = {
            'User-Agent': 'hogwarts'
        }
        cookie_data = {"hogwarts":"school",
                       "teacher":"AF"}
        r = requests.get(url=url, headers=header, cookies=cookie_data)
        print(r.request.headers)

    def test_oauth(self):
        r=requests.get(url="https://httpbin.testing-studio.com/basic-auth/apple/123",
                     auth=HTTPBasicAuth("apple","123"))
        print(r.text)

