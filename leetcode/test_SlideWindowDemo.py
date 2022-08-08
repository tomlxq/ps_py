#!/usr/bin/python
# -*- coding: utf-8 -*-
from unittest import TestCase
from SlideWindowDemo import SlideWindowDemo
import unittest
from collections import deque
import numpy as np


class TestSlideWindowDemo(unittest.TestCase):
    def test_find_max_average(self):
        self.assertEquals(12.75, SlideWindowDemo.findMaxAverage(self, [1, 12, -5, -6, 50, 3], 4))


if __name__ == '__main__':
    # verbosity=*：默认是1；设为0，则不输出每一个用例的执行结果；2-输出详细的执行结果
    unittest.main(verbosity=1)
    assert False
