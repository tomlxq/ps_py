#!/usr/bin/python
# -*- coding: utf-8 -*-
import unittest

from Martion import Martion


class test_Martion(unittest.TestCase):
    def test_fun1(self):
        self.assertEquals(226, Martion.func(self, ("7#6$5#12")))
        self.assertEquals(226, Martion.func2(self, ("7#6$5#12")))
