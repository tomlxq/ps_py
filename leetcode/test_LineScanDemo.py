#!/usr/bin/python
# -*- coding: utf-8 -*-
from unittest import TestCase
from LineScanDemo import LineScanDemo
import unittest
from collections import deque
import numpy as np


class TestLineScanDemo(unittest.TestCase):
    def test_maximum_product(self):
        self.assertEquals(6, LineScanDemo.maximumProduct(self, [1, 2, 3]))
        self.assertEquals(24, LineScanDemo.maximumProduct(self, [1, 2, 3, 4]))
        self.assertEquals(-6, LineScanDemo.maximumProduct(self, [-1, -2, -3]))
        self.assertEquals(39200, LineScanDemo.maximumProduct(self, [-100, -98, -1, 2, 3, 4]))
        self.assertEquals(300, LineScanDemo.maximumProduct(self, [-100, -2, -3, 1]))
        self.assertEquals(6, LineScanDemo.maximumProduct2(self, [1, 2, 3]))
        self.assertEquals(24, LineScanDemo.maximumProduct2(self, [1, 2, 3, 4]))
        self.assertEquals(-6, LineScanDemo.maximumProduct2(self, [-1, -2, -3]))
        self.assertEquals(39200, LineScanDemo.maximumProduct2(self, [-100, -98, -1, 2, 3, 4]))
        self.assertEquals(300, LineScanDemo.maximumProduct2(self, [-100, -2, -3, 1]))


