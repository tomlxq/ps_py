#!/usr/bin/python
# -*- coding: utf-8 -*-
import unittest

from RecursiveDemo import RecursiveDemo


class TestRecursiveDemo(unittest.TestCase):
    def test_predict_the_winner(self):
        self.assertFalse(RecursiveDemo.PredictTheWinner(self, [1, 5, 2]))
        self.assertTrue(RecursiveDemo.PredictTheWinner(self, [1, 5, 233, 7]))
        self.assertFalse(RecursiveDemo.PredictTheWinner4(self, [1, 5, 2]))
        self.assertTrue(RecursiveDemo.PredictTheWinner4(self, [1, 5, 233, 7]))

if __name__ == '__main__':
    # verbosity=*：默认是1；设为0，则不输出每一个用例的执行结果；2-输出详细的执行结果
    unittest.main(verbosity=1)

    assert False
