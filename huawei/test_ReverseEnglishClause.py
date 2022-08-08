#!/usr/bin/python
# -*- coding: utf-8 -*-
import unittest

from ReverseEnglishClause import ReverseEnglishClause


class test_ReverseEnglishClause(unittest.TestCase):
    def test_func(self):
        self.assertEquals("I a am developer.", ReverseEnglishClause.func(self, "I am a developer.", 1, 2))
        self.assertEquals("world! Hello", ReverseEnglishClause.func(self, "Hello world!", 0, 1))
        self.assertEquals("developer. a am I", ReverseEnglishClause.func(self, "I am a developer.", 0, 3))
        self.assertEquals("EMPTY", ReverseEnglishClause.func(self, "Hello!", 0, 3))


if __name__ == '__main__':
    # verbosity=*：默认是1；设为0，则不输出每一个用例的执行结果；2-输出详细的执行结果
    unittest.main(verbosity=1)

    assert False
