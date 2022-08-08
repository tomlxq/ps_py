#!/usr/bin/python
# -*- coding: utf-8 -*-
from unittest import TestCase

import unittest
from hello import Solution


class TestDemo(unittest.TestCase):
    """Test mathfuc.py"""

    @classmethod
    def setUpClass(cls):
        print("this setupclass() method only called once.\n")

    @classmethod
    def tearDownClass(cls):
        print("this teardownclass() method only called once too.\n")

    def setUp(self):
        print("do something before test : prepare environment.\n")

    def tearDown(self):
        print("do something after test : clean up.\n")

    def test_ladder_length(self):
        begin_word = "hit"
        end_word = "cog"
        word_list = ["hot", "dot", "dog", "lot", "log"]
        self.assertEqual(0, Solution.ladderLength(self, begin_word, end_word, word_list))
        word_list = ["hot", "dot", "dog", "lot", "log", "cog"]
        self.assertEqual(5, Solution.ladderLength(self, begin_word, end_word, word_list))

    def test_ladder_length2(self):
        begin_word = "hit"
        end_word = "cog"
        word_list = ["hot", "dot", "dog", "lot", "log"]
        self.assertEqual(0, Solution.ladderLength2(self, begin_word, end_word, word_list))
        word_list = ["hot", "dot", "dog", "lot", "log", "cog"]
        self.assertEqual(5, Solution.ladderLength2(self, begin_word, end_word, word_list))

    # def test_inorder_traversal(self):
    # res = Solution.inorderTraversal(self, list(1, None, 2, 3))
    #    print(res)

    def test_compute_area(self):
        self.assertEqual(45, Solution.computeArea(self, -3, 0, 3, 4, 0, -1, 9, 2))
        self.assertEqual(16, Solution.computeArea(self, -2, -2, 2, 2, -2, -2, 2, 2))
        self.assertEqual(45, Solution.computeArea2(self, -3, 0, 3, 4, 0, -1, 9, 2))
        self.assertEqual(16, Solution.computeArea2(self, -2, -2, 2, 2, -2, -2, 2, 2))

    def test_compress(self):
        self.assertEqual(4, Solution.compress(self, ["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"]))

    def test_last_remaining(self):
        self.assertEqual(3, Solution.lastRemaining(self, 5, 3))
        self.assertEqual(2, Solution.lastRemaining(self, 10, 17))
        self.assertEqual(3, Solution.lastRemaining1(self, 5, 3))
        self.assertEqual(2, Solution.lastRemaining1(self, 10, 17))
        self.assertEqual(3, Solution.lastRemaining2(self, 5, 3))
        self.assertEqual(2, Solution.lastRemaining2(self, 10, 17))

    def test_compress_string(self):
        self.assertEqual("a2b1c5a3", Solution.compressString(self, "aabcccccaaa"))
        self.assertEqual("abbccd", Solution.compressString(self, "abbccd"))
        self.assertEqual("a2b1c5a3", Solution.compressString2(self, "aabcccccaaa"))
        self.assertEqual("abbccd", Solution.compressString2(self, "abbccd"))

    def test_sum_stop_bus(self):
        self.assertEqual(5, Solution.sumStopBus(self,
                                                ['1', '1', '0', '0', '1', '1', '1', '0', '1', '1', '1', '1', '1', '1',
                                                 '1']))
        self.assertEqual(2, Solution.sumStopBus(self, ['1', '0', '1']))
        self.assertEqual(5, Solution.sumStopBus1(self,
                                                 ['1', '1', '0', '0', '1', '1', '1', '0', '1', '1', '1', '1', '1', '1',
                                                  '1']))
        self.assertEqual(2, Solution.sumStopBus1(self, ['1', '0', '1']))

    def test_decompress_string3(self):
        self.assertEqual("ddddff", Solution.decompressString3(self, "4dff"))
        self.assertEqual("!error", Solution.decompressString3(self, "2dff"))
        self.assertEqual("!error", Solution.decompressString3(self, "4d@A"))
        self.assertEqual("!error", Solution.decompressString3(self, "22aa"))
        self.assertEqual("aaabbccccd", Solution.decompressString3(self, "3abb4cd"))

    def test_has_path(self):
        maze = [[0, 0, 1, 0, 1], [0, 0, 0, 0, 0], [0, 0, 0, 1, 0], [1, 1, 0, 1, 1], [0, 0, 0, 0, 0]]
        start = [0, 4]
        destination = [3, 2]
        self.assertEqual(False, Solution.hasPath(self, maze, start, destination))
        self.assertEqual(True, Solution.hasPath(self, maze, start, [4, 4]))


if __name__ == '__main__':
    # verbosity=*：默认是1；设为0，则不输出每一个用例的执行结果；2-输出详细的执行结果
    unittest.main(verbosity=1)
