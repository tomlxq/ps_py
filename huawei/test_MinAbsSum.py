#!/usr/bin/python
# -*- coding: utf-8 -*-
import unittest

from MinAbsSum import MinAbsSum


class test_MinAbsSum(unittest.TestCase):
    def test_func(self):
        self.assertEquals("-3 5 2", MinAbsSum.func(self, "-1 -3 7 5 11 15"))
