#!/usr/bin/python
# -*- coding: utf-8 -*-
import unittest

from DfsBfsDemo import DfsBfsDemo
from TreeNode import TreeNode


class TestDfsBfsDemo(unittest.TestCase):
    def test_min_depth(self):
        left15 = TreeNode(15, None, None)
        right7 = TreeNode(7, None, None)
        right20 = TreeNode(20, left15, right7)
        left9 = TreeNode(9, None, None)
        tree_node = TreeNode(3, left9, right20)

        self.assertEquals(2, DfsBfsDemo.minDepth(self, tree_node))
        self.assertEquals(2, DfsBfsDemo.minDepth2(self, tree_node))

    def test_find_circle_num(self):
        self.assertEquals(2, DfsBfsDemo.findCircleNum(self, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
        self.assertEquals(3, DfsBfsDemo.findCircleNum(self, [[1, 0, 0], [0, 1, 0], [0, 0, 1]]))
        self.assertEquals(2, DfsBfsDemo.findCircleNum2(self, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
        self.assertEquals(3, DfsBfsDemo.findCircleNum2(self, [[1, 0, 0], [0, 1, 0], [0, 0, 1]]))
        self.assertEquals(2, DfsBfsDemo.findCircleNum3(self, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
        self.assertEquals(3, DfsBfsDemo.findCircleNum3(self, [[1, 0, 0], [0, 1, 0], [0, 0, 1]]))


if __name__ == '__main__':
    # verbosity=*：默认是1；设为0，则不输出每一个用例的执行结果；2-输出详细的执行结果
    unittest.main(verbosity=1)
    assert False
