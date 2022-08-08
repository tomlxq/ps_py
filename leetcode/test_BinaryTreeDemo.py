#!/usr/bin/python
# -*- coding: utf-8 -*-
import unittest

from BinaryTreeDemo import BinaryTreeExample
from TreeNode import TreeNode


class TestBinaryTreeDemo(unittest.TestCase):

    def test_binary_tree(self):
        node4 = TreeNode(4, None, None)
        node6 = TreeNode(6, None, None)
        node7 = TreeNode(7, None, None)
        node5 = TreeNode(5, node6, node7)
        node2 = TreeNode(2, node4, node5)
        node3 = TreeNode(3, None, None)
        node1 = TreeNode(1, node2, node3)
        list = [1, 2, 4, 5, 6, 7, 3]
        self.assertEquals(BinaryTreeExample.preorderTraversal(self, node1), list)
        self.assertEquals(BinaryTreeExample.preorderTraversal2(self, node1), list)
        self.assertEquals(BinaryTreeExample.preorderTraversal3(self, node1), list)

        list2 = [4, 2, 6, 5, 7, 1, 3]
        self.assertEquals(BinaryTreeExample.inorderTraversal(self, node1), list2)
        self.assertEquals(BinaryTreeExample.inorderTraversal2(self, node1), list2)
        self.assertEquals(BinaryTreeExample.inorderTraversal3(self, node1), list2)

        list3 = [4, 6, 7, 5, 2, 3, 1]
        self.assertEquals(BinaryTreeExample.postorderTraversal(self, node1), list3)
        self.assertEquals(BinaryTreeExample.postorderTraversal2(self, node1), list3)
        self.assertEquals(BinaryTreeExample.postorderTraversal3(self, node1), list3)


    def test_level_order(self):
        node4 = TreeNode(4, None, None)
        node6 = TreeNode(6, None, None)
        node7 = TreeNode(7, None, None)
        node5 = TreeNode(5, node6, node7)
        node2 = TreeNode(2, node4, node5)
        node3 = TreeNode(3, None, None)
        node1 = TreeNode(1, node2, node3)
        list4 = [[1], [2, 3], [4, 5], [6, 7]]
        self.assertEquals(BinaryTreeExample.levelOrder(self, node1), list4)
        self.assertEquals(BinaryTreeExample.levelOrder2(self, node1), list4)

        node22 = TreeNode(2, None, None)
        node11 = TreeNode(1, None, node22)
        list5 = [[1], [2]]
        self.assertEquals(BinaryTreeExample.levelOrder(self, node11), list5)
