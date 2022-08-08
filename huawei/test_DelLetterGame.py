#!/usr/bin/python
# -*- coding: utf-8 -*-
import unittest

from DelLetterGame import DelLetterGame


class test_DelLetterGame(unittest.TestCase):
    def test_fun(self):
        self.assertEquals(DelLetterGame.fun(self, "aaaaaaa"), 1)
        self.assertEquals(DelLetterGame.fun(self, "abcaacba"), 0)

        self.assertEquals(DelLetterGame.fun2(self, "aaaaaaa"), 1)
        self.assertEquals(DelLetterGame.fun2(self, "abcaacba"), 0)

        self.assertEquals(DelLetterGame.fun3(self, "aaaaaaa"), 1)
        self.assertEquals(DelLetterGame.fun3(self, "abcaacba"), 0)
