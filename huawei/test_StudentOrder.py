#!/usr/bin/python
# -*- coding: utf-8 -*-
import unittest

from StudentOrder import StudentOrder


class test_StudentOrder(unittest.TestCase):
    def test_func(self):
        self.assertEquals("2134", StudentOrder.func(self, 4, "100 100 120 130", "40 30 60 50"))
        self.assertEquals("132", StudentOrder.func(self, 3, "90 110 90", "45 60 45"))
