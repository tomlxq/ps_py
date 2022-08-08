#!/usr/bin/python
# -*- coding: utf-8 -*-
import unittest

from StudentCompare import StudentCompare


class test_StudentCompare(unittest.TestCase):
    def test_compare(self):
        self.assertEquals("99 101 98 102 97 103 96 104 95 105",
                          StudentCompare.compare(self, "100 10", "95 96 97 98 99 101 102 103 104 105"))


if __name__ == '__main__':
    # verbosity=*：默认是1；设为0，则不输出每一个用例的执行结果；2-输出详细的执行结果
    unittest.main(verbosity=1)

    assert False
