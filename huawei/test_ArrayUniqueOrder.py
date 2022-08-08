#!/usr/bin/python
# -*- coding: utf-8 -*-
import unittest

from ArrayUniqueOrder import ArrayUniqueOrder


class test_ArrayUniqueOrder(unittest.TestCase):
    def test_func(self):
        self.assertEquals("3,4,1,2,5", ArrayUniqueOrder.func(self, "1,3,3,3,2,4,4,4,5"))
