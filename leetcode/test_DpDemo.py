#!/usr/bin/python
# -*- coding: utf-8 -*-
from unittest import TestCase
from DpDemo import DpExample
import unittest
from collections import deque
import numpy as np


class TestDpDemo(unittest.TestCase):

    def test_climb_stairs(self):
        self.assertEquals(2, DpExample.climbStairs(self, 2))
        self.assertEquals(3, DpExample.climbStairs(self, 3))
        self.assertEquals(2, DpExample.climbStairs2(self, 2))
        self.assertEquals(3, DpExample.climbStairs2(self, 3))

    def test_num_squares(self):
        self.assertEquals(3, DpExample.numSquares(self, 12))
        self.assertEquals(2, DpExample.numSquares(self, 13))
        self.assertEquals(3, DpExample.numSquares2(self, 12))
        self.assertEquals(2, DpExample.numSquares2(self, 13))

    def test_minimum_total(self):
        self.assertEquals(11, DpExample.minimumTotal(self, [[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]))
        self.assertEquals(-10, DpExample.minimumTotal(self, [[-10]]))
        self.assertEquals(11, DpExample.minimumTotal2(self, [[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]))
        self.assertEquals(-10, DpExample.minimumTotal2(self, [[-10]]))

    def test_max_product(self):
        self.assertEquals(6, DpExample.maxProduct(self, [2, 3, -2, 4]))
        self.assertEquals(0, DpExample.maxProduct(self, [-2, 0, -1]))

    def test_max_profit(self):
        self.assertEquals(5, DpExample.maxProfit(self, [7, 1, 5, 3, 6, 4]))
        self.assertEquals(0, DpExample.maxProfit(self, [7, 6, 4, 3, 1]))
        self.assertEquals(5, DpExample.maxProfit2(self, [7, 1, 5, 3, 6, 4]))
        self.assertEquals(0, DpExample.maxProfit2(self, [7, 6, 4, 3, 1]))

    def test_max_profit122(self):
        self.assertEquals(7, DpExample.maxProfit122(self, [7, 1, 5, 3, 6, 4]))
        self.assertEquals(4, DpExample.maxProfit122(self, [1, 2, 3, 4, 5]))
        self.assertEquals(0, DpExample.maxProfit122(self, [7, 6, 4, 3, 1]))
        self.assertEquals(7, DpExample.maxProfit1222(self, [7, 1, 5, 3, 6, 4]))
        self.assertEquals(4, DpExample.maxProfit1222(self, [1, 2, 3, 4, 5]))
        self.assertEquals(0, DpExample.maxProfit1222(self, [7, 6, 4, 3, 1]))


if __name__ == '__main__':
    # verbosity=*：默认是1；设为0，则不输出每一个用例的执行结果；2-输出详细的执行结果
    unittest.main(verbosity=1)

    assert False
