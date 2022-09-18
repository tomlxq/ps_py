#!/usr/bin/python
# -*- coding: utf-8 -*-
from unittest import TestCase
from Leetcode70 import Leetcode70
import unittest
from collections import deque
import numpy as np


class TestLeetcode70(unittest.TestCase):

    def test_climb_stairs(self):
        self.assertEquals(2, Leetcode70.climbStairs(self, 2))
        self.assertEquals(3, Leetcode70.climbStairs(self, 3))
        self.assertEquals(2, Leetcode70.climbStairs2(self, 2))
        self.assertEquals(3, Leetcode70.climbStairs2(self, 3))
        self.assertEquals(2, Leetcode70.climbStairs3(self, 2))
        self.assertEquals(3, Leetcode70.climbStairs3(self, 3))

