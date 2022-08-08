#!/usr/bin/python
# -*- coding: utf-8 -*-
import unittest

from FindMinNum import FindMinNum


class test_FindMinNum(unittest.TestCase):
    def test_func(self):
        self.assertEquals("0", FindMinNum.func(self, "10", 1))
        self.assertEquals("200", FindMinNum.func(self, "10200", 1))
        self.assertEquals("131", FindMinNum.func(self, "2615371", 4))
