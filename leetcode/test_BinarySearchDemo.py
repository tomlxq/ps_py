#!/usr/bin/python
# -*- coding: utf-8 -*-
from unittest import TestCase
from BinarySearchDemo import BinarySearchExample
import unittest
from collections import deque
import numpy as np


class TestBinarySearchDemo(unittest.TestCase):
    def test_my_sqrt(self):
        self.assertEquals(5, BinarySearchExample.mySqrt(self, 25))
        self.assertEquals(4, BinarySearchExample.mySqrt(self, 24))
        self.assertEquals(5, BinarySearchExample.mySqrt2(self, 25))
        self.assertEquals(4, BinarySearchExample.mySqrt2(self, 24))

    def test_arrange_coins(self):
        self.assertEquals(0, BinarySearchExample.arrangeCoins(self, 0))
        self.assertEquals(1, BinarySearchExample.arrangeCoins(self, 1))
        self.assertEquals(2, BinarySearchExample.arrangeCoins(self, 5))
        self.assertEquals(3, BinarySearchExample.arrangeCoins(self, 8))
        self.assertEquals(60070, BinarySearchExample.arrangeCoins(self, 1804289383))

        self.assertEquals(0, BinarySearchExample.arrangeCoins2(self, 0))
        self.assertEquals(1, BinarySearchExample.arrangeCoins2(self, 1))
        self.assertEquals(2, BinarySearchExample.arrangeCoins2(self, 5))
        self.assertEquals(3, BinarySearchExample.arrangeCoins2(self, 8))
        self.assertEquals(60070, BinarySearchExample.arrangeCoins2(self, 1804289383))

        self.assertEquals(0, BinarySearchExample.arrangeCoins3(self, 0))
        self.assertEquals(1, BinarySearchExample.arrangeCoins3(self, 1))
        self.assertEquals(2, BinarySearchExample.arrangeCoins3(self, 5))
        self.assertEquals(3, BinarySearchExample.arrangeCoins3(self, 8))
        self.assertEquals(60070, BinarySearchExample.arrangeCoins3(self, 1804289383))
        self.assertEquals(0, BinarySearchExample.arrangeCoins4(self, 0))
        self.assertEquals(1, BinarySearchExample.arrangeCoins4(self, 1))
        self.assertEquals(2, BinarySearchExample.arrangeCoins4(self, 5))
        self.assertEquals(3, BinarySearchExample.arrangeCoins4(self, 8))
        self.assertEquals(60070, BinarySearchExample.arrangeCoins4(self, 1804289383))
        self.assertEquals(0, BinarySearchExample.arrangeCoins5(self, 0))
        self.assertEquals(1, BinarySearchExample.arrangeCoins5(self, 1))
        self.assertEquals(2, BinarySearchExample.arrangeCoins5(self, 5))
        self.assertEquals(3, BinarySearchExample.arrangeCoins5(self, 8))
        self.assertEquals(60070, BinarySearchExample.arrangeCoins5(self, 1804289383))


