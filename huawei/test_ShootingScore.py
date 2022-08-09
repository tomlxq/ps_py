#!/usr/bin/python
# -*- coding: utf-8 -*-
import unittest

from ShootingScore import ShootingScore


class test_ShootingScore(unittest.TestCase):
    def test_func(self):
        self.assertEquals("5,3,7,4", ShootingScore.func(self, 13, "3,3,7,4,4,4,4,7,7,3,5,5,5",
                                                        "53,80,68,24,39,76,66,16,100,55,53,80,55"))
