#!/usr/bin/python
# -*- coding: utf-8 -*-
import unittest

from MiniStopBus import MiniStopBus


class test_MiniStopBus(unittest.TestCase):
    def test_func(self):
        self.assertEquals(2, MiniStopBus.func(self, "1,0,1"))
        self.assertEquals(3, MiniStopBus.func(self, "1,1,0,0,1,1,1,0,1"))
        self.assertEquals(2, MiniStopBus.func2(self, "1,0,1"))
        self.assertEquals(3, MiniStopBus.func2(self, "1,1,0,0,1,1,1,0,1"))
