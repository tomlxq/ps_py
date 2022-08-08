#!/usr/bin/python
# -*- coding: utf-8 -*-
from unittest import TestCase
from EratosthenesDemo import EratosthenesDemo
import unittest
from collections import deque
import numpy as np


class TestBfDemo(unittest.TestCase):
    def test_count_primes(self):
        self.assertEqual(4, EratosthenesDemo.countPrimes(self, 10))
        self.assertEqual(0, EratosthenesDemo.countPrimes(self, 1))
        self.assertEqual(0, EratosthenesDemo.countPrimes(self, 0))
        self.assertEqual(4, EratosthenesDemo.countPrimes2(self, 10))
        self.assertEqual(0, EratosthenesDemo.countPrimes2(self, 1))
        self.assertEqual(0, EratosthenesDemo.countPrimes2(self, 0))
