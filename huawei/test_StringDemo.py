#!/usr/bin/python
# -*- coding: utf-8 -*-
import unittest

from StringDemo import StringDemo


class test_StringDemo(unittest.TestCase):

    def test_search_string(self):
        self.assertEquals(3, StringDemo.findString(self, "abc", "abcaybec"))
        self.assertEquals(3, StringDemo.findString2(self, "abc", "abcaybec"))
