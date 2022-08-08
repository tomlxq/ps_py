#!/usr/bin/python
# -*- coding: utf-8 -*-
from unittest import TestCase
from list_demo import ListDemo
from ListNode import ListNode
import unittest
from collections import deque
import numpy as np


class TestListDemo(unittest.TestCase):

    def setUp(self) -> None:
        node5 = ListNode(5, None)
        node4 = ListNode(4, node5)
        node3 = ListNode(3, node4)
        node2 = ListNode(2, node3)
        node1 = ListNode(1, node2)
        self.test_data = node1

    def test_reverse_list(self):
        prev = ListDemo.reverseList(self, self.test_data)
        self.assertEquals(5, prev.val)
        self.assertEquals(4, prev.next.val)

    def test_reverse_list2(self):
        prev = ListDemo.reverseList2(self, self.test_data)
        self.assertEquals(5, prev.val)
        self.assertEquals(4, prev.next.val)

    def test_has_cycle(self):
        l4 = ListNode(-4, None)
        l0 = ListNode(0, l4)
        l2 = ListNode(2, l0)
        l3 = ListNode(3, l2)
        l4.next = l2
        self.assertTrue(ListDemo.hasCycle(self, l3))
        node2 = ListNode(2, None)
        node1 = ListNode(2, node2)
        node2.next = node1
        self.assertTrue(ListDemo.hasCycle2(self, node1))


if __name__ == '__main__':
    # verbosity=*：默认是1；设为0，则不输出每一个用例的执行结果；2-输出详细的执行结果
    unittest.main(verbosity=1)
    assert False
