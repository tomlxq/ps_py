#!/usr/bin/python
# -*- coding: utf-8 -*-
from unittest import TestCase
from DoublePointDemo import DoublePointExample
import unittest
from collections import deque
import numpy as np


class TestDoublePointDemo(unittest.TestCase):
    def test_remove_duplicates(self):
        self.assertEquals(2, DoublePointExample.removeDuplicates(self, [1, 1, 2]))
        self.assertEquals(5, DoublePointExample.removeDuplicates(self, [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))

    def test_pivot_index(self):
        self.assertEquals(3, DoublePointExample.pivotIndex(self, [1, 7, 3, 6, 5, 6]))
        self.assertEquals(-1, DoublePointExample.pivotIndex(self, [1, 2, 3]))
        self.assertEquals(0, DoublePointExample.pivotIndex(self, [2, 1, -1]))
        self.assertEquals(3, DoublePointExample.pivotIndex2(self, [1, 7, 3, 6, 5, 6]))
        self.assertEquals(-1, DoublePointExample.pivotIndex2(self, [1, 2, 3]))
        self.assertEquals(0, DoublePointExample.pivotIndex2(self, [2, 1, -1]))

    def test_merge(self):
        ary = [1, 2, 3, 0, 0, 0]
        DoublePointExample.merge(self, ary, 3, [2, 5, 6], 3)
        self.assertEquals(ary, [1, 2, 2, 3, 5, 6])
        ary2 = [1, 2, 3, 0, 0, 0]
        DoublePointExample.merge2(self, ary2, 3, [2, 5, 6], 3)
        self.assertEquals(ary2, [1, 2, 2, 3, 5, 6])
        ary3 = [1, 2, 3, 0, 0, 0]
        DoublePointExample.merge3(self, ary3, 3, [2, 5, 6], 3)
        self.assertEquals(ary3, [1, 2, 2, 3, 5, 6])

