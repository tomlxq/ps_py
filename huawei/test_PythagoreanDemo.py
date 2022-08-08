#!/usr/bin/python
# -*- coding: utf-8 -*-
import unittest

from PythagoreanDemo import PythagoreanDemo


class test_PythagoreanDemo(unittest.TestCase):
    def test_func(self):
        self.assertEquals("3 4 5\n5 12 13\n8 15 17", PythagoreanDemo.func(self, 1, 20))
        self.assertEquals("Na", PythagoreanDemo.func(self, 5, 10))
