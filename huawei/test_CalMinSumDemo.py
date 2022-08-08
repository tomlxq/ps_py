#!/usr/bin/python
# -*- coding: utf-8 -*-
import unittest

from CalMinSumDemo import CalMinSumDemo


class test_CalMinSumDemo(unittest.TestCase):
    def test_func(self):
        self.assertEquals(CalMinSumDemo.func(self, "3 1 1 2", "3 1 2 3", 2), 4)
        self.assertEquals(CalMinSumDemo.func(self, "3 1 3 4", "3 1 2 3", 4), 13)
