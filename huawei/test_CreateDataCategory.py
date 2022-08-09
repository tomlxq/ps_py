#!/usr/bin/python
# -*- coding: utf-8 -*-
import unittest

from CreateDataCategory import CreateDataCategory


class TestLineScanDemo(unittest.TestCase):
    def test_func(self):
        self.assertEquals(5, CreateDataCategory.func(self, "5 2 1 2 3 4 5 6 7 8 9 10"))
