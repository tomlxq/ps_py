#!/usr/bin/python
# -*- coding: utf-8 -*-
import unittest

from MiniAbsArray import MiniAbsArray


class test_MiniAbsArray(unittest.TestCase):
    def test_func(self):
        self.assertEquals("-3 5 2", MiniAbsArray.func(self, "-1 -3 7 5 11 15"))
