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

    def test_two_sum(self):
        self.assertEquals(LineScanDemo.twoSum(self, [2, 7, 11, 15], 9), [0, 1])
        self.assertEquals(LineScanDemo.twoSum(self, [3, 2, 4], 6), [1, 2])
        self.assertEquals(LineScanDemo.twoSum(self, [3, 3], 6), [0, 1])
        self.assertEquals(LineScanDemo.twoSum2(self, [2, 7, 11, 15], 9), [0, 1])
        self.assertEquals(LineScanDemo.twoSum2(self, [3, 2, 4], 6), [1, 2])
        self.assertEquals(LineScanDemo.twoSum2(self, [3, 3], 6), [0, 1])

        self.assertEquals(LineScanDemo.twoSum3(self, [2, 7, 11, 15], 9), [1, 2])
        self.assertEquals(LineScanDemo.twoSum3(self, [2, 3, 4], 6), [1, 3])
        self.assertEquals(LineScanDemo.twoSum3(self, [-1, 0], -1), [1, 2])
        self.assertEquals(LineScanDemo.twoSum4(self, [2, 7, 11, 15], 9), [1, 2])
        self.assertEquals(LineScanDemo.twoSum4(self, [2, 3, 4], 6), [1, 3])
        self.assertEquals(LineScanDemo.twoSum4(self, [-1, 0], -1), [1, 2])
