#!/usr/bin/python
# -*- coding: utf-8 -*-
import unittest

from MaxBracketNum import MaxBracketNum


class test_MaxBracketNum(unittest.TestCase):
    def test_func(self):
        self.assertEquals(1, MaxBracketNum.func(self, "[]"))
        self.assertEquals(3, MaxBracketNum.func(self, "{ooo[cccc(ccc)ccc]}"))
        self.assertEquals(0, MaxBracketNum.func(self, "{ooo[cccc(ccc]ccc]}"))