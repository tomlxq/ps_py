#!/usr/bin/python
# -*- coding: utf-8 -*-
import unittest

from PrintOrder import PrintOrder


class test_PrintOrder(unittest.TestCase):
    def test_func(self):
        self.assertEquals("0,2,1", PrintOrder.func(self, "9,3,5"))
        self.assertEquals("2,0,1", PrintOrder.func(self, "1,2,2"))
        self.assertEquals("0,2,3,4,1", PrintOrder.func(self, "9,3,3,3,5"))


if __name__ == '__main__':
    # verbosity=*：默认是1；设为0，则不输出每一个用例的执行结果；2-输出详细的执行结果
    unittest.main(verbosity=1)

    assert False


def test_func():
    assert False
