# !/usr/bin/python
# -*- coding: utf-8 -*-
import unittest

from GreedyDemo import GreedyDemo


class TestGreedyDemo(unittest.TestCase):
    def test_find_length_of_lcis(self):
        self.assertEquals(3, GreedyDemo.findLengthOfLCIS(self, [1, 3, 5, 4, 7]))
        self.assertEquals(1, GreedyDemo.findLengthOfLCIS(self, [2, 2, 2, 2, 2]))

    def test_lemonade_change(self):
        self.assertTrue(GreedyDemo.lemonadeChange(self, [5, 5, 5, 10, 20]))
        self.assertFalse(GreedyDemo.lemonadeChange(self, [5, 5, 10, 10, 20]))

    def test_largest_perimeter(self):
        self.assertEquals(5, GreedyDemo.largestPerimeter(self, [2, 1, 2]))
        self.assertEquals(0, GreedyDemo.largestPerimeter(self, [1, 2, 1]))


if __name__ == '__main__':
    # verbosity=*：默认是1；设为0，则不输出每一个用例的执行结果；2-输出详细的执行结果
    unittest.main(verbosity=1)
    assert False
