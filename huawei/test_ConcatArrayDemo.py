#!/usr/bin/python
# -*- coding: utf-8 -*-
import unittest

from ConcatArrayDemo import ConcatArrayDemo


class test_ConcatArrayDemo(unittest.TestCase):
    def test_func(self):
        self.assertEquals("2,5,6,1,7,4,7,9,5,3,4,7", ConcatArrayDemo.func(self, ["2,5,6,7,9,5,7", "1,7,4,3,4"], 3));
        self.assertEquals("1,2,3,4,1,2,3,1,2,3,4,5,6",
                          ConcatArrayDemo.func(self, ["1,2,3,4,5,6", "1,2,3", "1,2,3,4"], 4));
