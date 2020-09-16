# !/usr/bin/env Python3
# -*- coding: utf-8 -*-
# @FILE     : test_unittest.py
# @Author   : Pluto.
# @Time     : 2020/9/10 16:22
import unittest

class demo(unittest.TestCase):

    def setUp(self) -> None:
        print("setup")
    def tearDown(self) -> None:
        print("teardowm")
    @classmethod
    def setUpClass(cls) -> None:
        print("set up class")
    @classmethod
    def tearDownClass(cls) -> None:
        print("tear dowm class")

    def test_abc(self):
        print("test abc")

    def test_upper(self):
        print("test_upper 111")
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        print("test_isupper 222")
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        print("test_split 333")
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    unittest.main()
