#!/usr/bin/python
# -*- coding: utf-8 -*-
from unittest import TestCase
from FibonacciDemo import FibonacciDemo
import unittest
from collections import deque
import numpy as np


class TestFibonacciDemo(unittest.TestCase):
    def test_fibonacci(self):
        self.assertEquals(0, FibonacciDemo.fibonacci(self, 0))
        self.assertEquals(55, FibonacciDemo.fibonacci(self, 10))
        self.assertEquals(0, FibonacciDemo.fibonacci2(self, 0))
        self.assertEquals(55, FibonacciDemo.fibonacci2(self, 10))
        self.assertEquals(0, FibonacciDemo.fibonacci3(self, 0))
        self.assertEquals(55, FibonacciDemo.fibonacci3(self, 10))
        self.assertEquals(0, FibonacciDemo.fibonacci4(self, 0))
        self.assertEquals(55, FibonacciDemo.fibonacci4(self, 10))
        self.assertEquals(0, FibonacciDemo.fibonacci5(self, 0))
        self.assertEquals(55, FibonacciDemo.fibonacci5(self, 10))
        self.assertEquals(0, FibonacciDemo.fibonacci6(self, 0))
        self.assertEquals(55, FibonacciDemo.fibonacci6(self, 10))
