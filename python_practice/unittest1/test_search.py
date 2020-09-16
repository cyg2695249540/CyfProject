# !/usr/bin/env Python3
# -*- coding: utf-8 -*-
# @FILE     : test_search.py
# @Author   : Pluto.
# @Time     : 2020/9/10 16:42
import unittest


class Search():
    def search_fun(self):
        print("search")
        return True

class TestSearch1(unittest.TestCase):
    # @classmethod
    # def setUpClass(cls) -> None:
    #     print("set up class")
    #     cls.search =Search()
    # @classmethod
    # def tearDownClass(cls) -> None:
    #     print("tear dowm class")
    def setUp(self) -> None:
        print("setup")
        self.search = Search()
    def tearDown(self) -> None:
        print("teardowm")

    def test_search1(self):
        print("testsearch1")
        assert True == self.search.search_fun()
    def test_search2(self):
        print("testsearch2")
        assert True == self.search.search_fun()
    def test_search3(self):
        print("testsearch3")
        assert True == self.search.search_fun()

class TestSearch2(unittest.TestCase):
    # @classmethod
    # def setUpClass(cls) -> None:
    #     print("set up class")
    #     cls.search =Search()
    # @classmethod
    # def tearDownClass(cls) -> None:
    #     print("tear dowm class")
    def setUp(self) -> None:
        print("setup")
        self.search = Search()
    def tearDown(self) -> None:
        print("teardowm")

    def test_search1(self):
        print("testsearch4")
        assert True == self.search.search_fun()
    def test_search2(self):
        print("testsearch5")
        assert True == self.search.search_fun()
    def test_search3(self):
        print("testsearch6")
        assert True == self.search.search_fun()

if __name__ == '__main__':
    unittest.main()