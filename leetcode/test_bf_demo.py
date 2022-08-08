#!/usr/bin/python
# -*- coding: utf-8 -*-
from unittest import TestCase
from bf_demo import BfDemo
import unittest
from collections import deque
import numpy as np


class TestBfDemo(unittest.TestCase):

    def test_ladder_length(self):
        begin_word = "hit"
        end_word = "cog"
        word_list = ["hot", "dot", "dog", "lot", "log"]
        self.assertEqual(0, BfDemo.ladder_length(self, begin_word, end_word, word_list))
        self.assertEqual(0, BfDemo.ladder_length2(self, begin_word, end_word, word_list))
        word_list = ["hot", "dot", "dog", "lot", "log", "cog"]
        self.assertEqual(5, BfDemo.ladder_length(self, begin_word, end_word, word_list))
        self.assertEqual(5, BfDemo.ladder_length2(self, begin_word, end_word, word_list))

    def test_has_path(self):
        maze1 = [[0, 0, 1, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 1, 0], [1, 1, 0, 1, 1], [0, 0, 0, 0, 0]]
        start = [0, 4]
        destination = [4, 4]
        self.assertTrue(BfDemo.hasPath(self, maze1, start, destination))
        maze2 = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 1, 0], [1, 1, 0, 1, 1], [0, 0, 0, 0, 0]]
        self.assertFalse(BfDemo.hasPath(self, maze2, start, [3, 2]))
        self.assertTrue(BfDemo.hasPath2(self, maze1, start, destination))
        self.assertFalse(BfDemo.hasPath2(self, maze2, start, [3, 2]))

    def test_find_the_city(self):
        self.assertEquals(3, BfDemo.findTheCity(self, 4, [[0, 1, 3], [1, 2, 1], [1, 3, 4], [2, 3, 1]], 4))
        self.assertEquals(0, BfDemo.findTheCity(self, 5,
                                                [[0, 1, 2], [0, 4, 8], [1, 2, 3], [1, 4, 2], [2, 3, 1], [3, 4, 1]], 2))

    def test_can_visit_all_rooms(self):
        self.assertTrue(BfDemo.canVisitAllRooms(self, [[1], [2], [3], []]))
        self.assertFalse(BfDemo.canVisitAllRooms(self, [[1, 3], [3, 0, 1], [2], [0]]))
        self.assertTrue(BfDemo.canVisitAllRooms2(self, [[1], [2], [3], []]))
        self.assertFalse(BfDemo.canVisitAllRooms2(self, [[1, 3], [3, 0, 1], [2], [0]]))

    def test_minimum_moves(self):
        queue = deque()
        queue.append(1)
        queue.append(2)
        print(queue.pop())
        self.assertEquals(11, BfDemo.minimumMoves(self, [[0, 0, 0, 0, 0, 1], [1, 1, 0, 0, 1, 0], [0, 0, 0, 0, 1, 1],
                                                         [0, 0, 1, 0, 1, 0], [0, 1, 1, 0, 0, 0], [0, 1, 1, 0, 0, 0]]))

    def test_min_path_sum(self):
        self.assertEquals(7, BfDemo.minPathSum(self, [[1, 3, 1], [1, 5, 1], [4, 2, 1]]))
        self.assertEquals(12, BfDemo.minPathSum(self, [[1, 2, 3], [4, 5, 6]]))



    def test_unique_paths(self):
        self.assertEquals(28, BfDemo.uniquePaths(self, 3, 7))
        self.assertEquals(3, BfDemo.uniquePaths(self, 3, 2))
        self.assertEquals(28, BfDemo.uniquePaths2(self, 3, 7))
        self.assertEquals(3, BfDemo.uniquePaths2(self, 3, 2))

    def test_unique_paths_with_obstacles(self):
        self.assertEquals(1, BfDemo.uniquePathsWithObstacles(self, [[0]]))
        self.assertEquals(0, BfDemo.uniquePathsWithObstacles(self, [[1, 0]]))
        self.assertEquals(2, BfDemo.uniquePathsWithObstacles(self, [[0, 0, 0], [0, 1, 0], [0, 0, 0]]))
        self.assertEquals(1, BfDemo.uniquePathsWithObstacles(self, [[0, 1], [0, 0]]))
        self.assertEquals(1, BfDemo.uniquePathsWithObstacles2(self, [[0]]))
        self.assertEquals(0, BfDemo.uniquePathsWithObstacles2(self, [[1, 0]]))
        self.assertEquals(2, BfDemo.uniquePathsWithObstacles2(self, [[0, 0, 0], [0, 1, 0], [0, 0, 0]]))
        self.assertEquals(1, BfDemo.uniquePathsWithObstacles2(self, [[0, 1], [0, 0]]))

    def test_select_sort(self):
        ary = [3, 1, 5, 6, 100, 88, 3, 2, 1]
        check_ary = ary.copy()
        check_ary.sort()
        BfDemo.insertSort(self, ary)
        print(check_ary)
        print(ary)
        self.assertTrue(np.array_equal(ary, check_ary))
        size=5
        for i in range(size - 1, size):
            print(i)

        ary = [3, 1, 5, 6, 100, 88, 3, 2, 1]
        BfDemo.bubbleSort(self, ary)
        print(check_ary)
        print(ary)
        self.assertTrue(np.array_equal(ary, check_ary))

        ary = [3, 1, 5, 6, 100, 88, 3, 2, 1]
        BfDemo.selectSort(self, ary)
        print(check_ary)
        print(ary)
        self.assertTrue(np.array_equal(ary, check_ary))


if __name__ == '__main__':
    # verbosity=*：默认是1；设为0，则不输出每一个用例的执行结果；2-输出详细的执行结果
    unittest.main(verbosity=1)

    assert False
