#!/usr/bin/python
# -*- coding: utf-8 -*-
import unittest

from Leetcode1 import Leetcode1


class TestLeetcode1(unittest.TestCase):
    def test_two_sum(self):
        self.assertEquals(Leetcode1.twoSum(self, [2, 7, 11, 15], 9), [0, 1])
        self.assertEquals(Leetcode1.twoSum(self, [3, 2, 4], 6), [1, 2])
        self.assertEquals(Leetcode1.twoSum(self, [3, 3], 6), [0, 1])
        self.assertEquals(Leetcode1.twoSum2(self, [2, 7, 11, 15], 9), [0, 1])
        self.assertEquals(Leetcode1.twoSum2(self, [3, 2, 4], 6), [1, 2])
        self.assertEquals(Leetcode1.twoSum2(self, [3, 3], 6), [0, 1])
        self.assertEquals(Leetcode1.twoSum3(self, [2, 7, 11, 15], 9), [1, 2])
        self.assertEquals(Leetcode1.twoSum3(self, [2, 3, 4], 6), [1, 3])
        self.assertEquals(Leetcode1.twoSum3(self, [-1, 0], -1), [1, 2])
        self.assertEquals(Leetcode1.twoSum4(self, [2, 7, 11, 15], 9), [1, 2])
        self.assertEquals(Leetcode1.twoSum4(self, [2, 3, 4], 6), [1, 3])
        self.assertEquals(Leetcode1.twoSum4(self, [-1, 0], -1), [1, 2])
