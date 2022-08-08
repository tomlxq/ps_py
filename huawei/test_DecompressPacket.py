#!/usr/bin/python
# -*- coding: utf-8 -*-
import unittest

from DecompressPacket import DecompressPacket


class test_DecompressPacket(unittest.TestCase):
    def test_func(self):
        self.assertEquals("kkkmnmn", DecompressPacket.func(self, "3[k]2[mn]"))
        self.assertEquals("mccmccmcc", DecompressPacket.func(self, "3[m2[c]]"))
