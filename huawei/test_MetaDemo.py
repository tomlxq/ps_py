#!/usr/bin/python
# -*- coding: utf-8 -*-
import unittest

from MetaDemo import MetaDemo


class test_MetaDemo(unittest.TestCase):
    def test_func(self):
        self.assertEquals(MetaDemo.fun2(self, 0, "asdbuiodevauufgh"), 3)
        self.assertEquals(MetaDemo.fun2(self, 2, "aeueo"), 0)
        self.assertEquals(MetaDemo.fun2(self, 1, "aabeebuu"), 5)
        self.assertEquals(MetaDemo.fun(self, 0, "asdbuiodevauufgh"), 3)
        self.assertEquals(MetaDemo.fun(self, 2, "aeueo"), 0)
        self.assertEquals(MetaDemo.fun(self, 1, "aabeebuu"), 5)
