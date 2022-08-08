#!/usr/bin/python
# -*- coding: utf-8 -*-
import unittest

from ConcatWord import ConcatWord


class test_ConcatWord(unittest.TestCase):
    def test_func(self):
        self.assertEquals("worddwordda", ConcatWord.func(self, 0, "word dd da dc dword d"))
        self.assertEquals("dwordda", ConcatWord.func(self, 4, "word dd da dc dword d"))
