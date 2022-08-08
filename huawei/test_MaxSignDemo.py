#!/usr/bin/python
# -*- coding: utf-8 -*-
import unittest

from MaxSignDemo import MaxSignDemo


class test_MaxSignDemo(unittest.TestCase):
    def test_func(self):
        self.assertEquals("01010", MaxSignDemo.func(self, "00101010101100001010010"))
        self.assertEquals("-1", MaxSignDemo.func(self, "0110"))
