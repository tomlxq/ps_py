from typing import List, Optional
from collections import deque

# from TreeNode import TreeNode
from TreeNode import TreeNode
import re


class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        visited = set()
        dirs = [0, 1, 0, -1, 0]
        row, col = len(maze), len(maze[0])

        # DFS
        def dfs(i, j):
            if i == destination[0] and j == destination[1]:
                return True
            for k in range(4):
                move_i, move_j = i, j
                while 0 <= (t1 := move_i + dirs[k]) < row and 0 <= (t2 := move_j + dirs[k + 1]) < col and maze[t1][
                    t2] != 1:
                    move_i, move_j = t1, t2
                if i == move_i and j == move_j: continue
                if (move_i, move_j) not in visited:
                    visited.add((move_i, move_j))
                    if dfs(move_i, move_j): return True
            return False

        # bfs
        def bfs(i, j):
            queue = deque([[i, j]])
            visited.add((i, j))
            while queue:
                i, j = queue.pop()
                if [i, j] == destination: return True
                for k in range(4):
                    move_i, move_j = i, j
                    while 0 <= (t1 := move_i + dirs[k]) < row and 0 <= (t2 := move_j + dirs[k + 1]) < col and maze[t1][
                        t2] != 1:
                        move_i, move_j = t1, t2
                    if move_i == i and move_j == j: continue
                    if (move_i, move_j) not in visited:
                        visited.add((move_i, move_j))
                        queue.appendleft([move_i, move_j])
            return False

        return dfs(start[0], start[1])  # bfs(start[0], start[1])

    def decompressString3(self, s: str) -> str:
        # //字符匹配：非法字符、类似“2aa”、类似“aaa”、以数字结尾的情况
        if re.search("[^0-9a-z]+", s) or re.search("[0-9]([a-z])\\1", s) or re.search("([a-z])\\1{2,}", s) or re.search(
                "[0-9]+$", s):
            return "!error"
        chars = list(s)
        size = len(chars)
        ret = []
        read = 0
        while read < size:
            if str(chars[read]).isalpha():
                ret.append(chars[read])
                read += 1
            else:
                start = read
                while str(chars[read]).isdigit():
                    read += 1
                tmp = int(s[start:read])
                if tmp == 2:
                    return "!error"
                for i in range(tmp):
                    ret.append(chars[read])
                read += 1
        return ''.join(ret)

    def sumStopBus1(self, nums: List[int]) -> List[int]:
        s = ''.join(nums).replace("111", "3").replace("11", "2")
        return s.count("3") + s.count("2") + s.count("1")

    def sumStopBus(self, nums: List[int]) -> List[int]:
        left = total = 0
        size = len(nums)
        for read in range(size):
            if read == size - 1 or nums[read] != nums[read + 1]:
                if nums[read] == '0':
                    left = read + 1
                    continue
                num = read - left + 1
                big = int(num / 3)
                mid = int((num - big * 3) / 2)
                small = num - big * 3 - mid * 2
                total += (big + small + mid)
                left = read + 1
        return total

    def compressString2(self, S: str) -> str:
        res = []
        i = j = 0
        size = len(S)
        chars = list(S)
        while i < size:
            while j < size and chars[i] == chars[j]:
                j += 1
            res.append("%s%s" % (chars[i], j - i))
            i = j
        ret = ''.join(res)
        if len(ret) >= size:
            return S
        return ret

    def compressString(self, S: str) -> str:
        res = ""
        chars = list(S)
        size = len(chars)
        left = 0
        for read in range(size):
            if read == size - 1 or chars[read] != chars[read + 1]:
                res += chars[read]
                num = read - left + 1
                res += str(num)
                left = read + 1
        if len(res) >= size:
            return S
        return res

    def decompressRLElist2(self, nums: List[int]) -> List[int]:
        # 最推荐这个做法
        # 思路是，将奇数和偶数位置的数分开成两个列表
        # nums[::2] 是反复次数，nums[1::2]是要出现的数
        # 包装在一起，提取出每个数和其对应的出现次数
        # for i,j in zip(nums[1::2],nums[::2])
        # 显示这个数，并且反复相应的次数
        # [i for i,j in zip(nums[1::2],nums[::2]) for _ in range(j)]
        return [i for i, j in zip(nums[1::2], nums[::2]) for _ in range(j)]

    def decompressRLElist(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(0, len(nums), 2):
            for j in range(nums[i]):
                res.append(nums[i + 1])
        return res

    def lastRemaining2(self, n: int, m: int) -> int:
        value = 0
        for i in range(1, n + 1):
            value = (value + m) % i
        return value

    def lastRemaining1(self, n: int, m: int) -> int:
        def last_remaining(len, k):
            if len == 1:
                return 0
            return (last_remaining(len - 1, k) + k) % len

        return last_remaining(n, m)

    def lastRemaining(self, n: int, m: int) -> int:
        if m == 1:
            return n - 1
        list_data = list()
        for i in range(n):
            list_data.insert(i, i)
        idx = 0
        while len(list_data) > 1:
            idx = (idx + m - 1) % len(list_data)
            list_data.pop(idx)
        return list_data[0]

    def compress(self, chars: List[str]) -> int:
        # 1.定义三个变量,read，write,left
        # 2.仅当前位为数据长度-1或不等于下一位时才更改数组
        # 3.具体操作，把当前位赋能write位；
        # 4.上一次位置与当前的位置差距read-left+1,跟据规则若为1，不写入，大于1，依赖写入write位
        write = left = 0
        size = len(chars)
        for read in range(size):
            if read == size - 1 or chars[read] != chars[read + 1]:
                chars[write] = chars[read]
                write += 1
                num = read - left + 1
                if num > 1:
                    print("%d %d" % (num, read))
                    tmp = str(num)
                    for c in tmp:
                        chars[write] = c
                        write += 1
                left = read + 1
        return write

    def computeArea2(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        def erea(x1, y1, x2, y2):
            if x2 <= x1 or y2 <= y1:
                return 0
            return (x2 - x1) * (y2 - y1)

        a = erea(ax1, ay1, ax2, ay2)
        b = erea(bx1, by1, bx2, by2)
        c = erea(max(ax1, bx1), max(ay1, by1), min(ax2, bx2), min(ay2, by2))
        return a + b - c

    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        a = (ax2 - ax1) * (ay2 - ay1)
        b = (bx2 - bx1) * (by2 - by1)
        c = max(0, min(ax2, bx2) - max(ax1, bx1)) * max(0, min(ay2, by2) - max(ay1, by1))
        return a + b - c



    def ladderLength2(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # 1.把wordList放在单词的hash列表word_set中，并判断是否为空，是否包括endWord
        word_set = set(wordList)
        if len(word_set) == 0 or endWord not in word_set:
            return 0
        if beginWord in word_set:
            word_set.remove(beginWord)
        # 2.双向广度优先遍历需要三个hash表，begin_set,end_set,visited_set，begin_set加入起始单词，end_set加放endWord,初始的扩散为1
        begin_set = set()
        begin_set.add(beginWord)
        end_set = set()
        end_set.add(endWord)
        visited_set = set()
        visited_set.add(beginWord)
        visited_set.add(endWord)
        step = 1
        # 3.对begin_set,end_set的处理，增加一个新的next_level_visited_set用于下一轮的循环
        # ①begin_set,end_set hash列表不为空，进行循环
        while begin_set and end_set:
            next_level_set = set()
            # ②begin_set,end_set比较小大，用小的来扩散，考虑的范围更小
            if len(begin_set) > len(end_set):
                begin_set, end_set = end_set, begin_set
            # ③循环begin_set每个单词，并针对每个单词的位置用26个字母替换，当替换字母为非本身字母时，进行下一步
            for word in begin_set:
                chars = list(word)
                word_size = len(chars)
                for j in range(word_size):
                    original_char = chars[j]
                    for k in range(26):
                        cur_char = chr(ord('a') + k)
                        if cur_char == original_char:
                            continue
                        chars[j] = cur_char
                        next_word = ''.join(chars)
                        # ④若在单词列表word_set中，判断是否在end_set，若在直接return step+1
                        if next_word in word_set:
                            if next_word in end_set:
                                return step + 1
                            # ⑤若在单词列表word_set中，不在end_set，判断是否在visited_set，不在加入next_level_visited_set，也加入visited_set
                            if next_word not in visited_set:
                                next_level_set.add(next_word)
                                visited_set.add(next_word)
                    # 恢复单词
                    chars[j] = original_char
            # ⑥next_level_visited_set赋给begin_set，step+1进行一下轮循环
            begin_set = next_level_set
            step += 1
        return 0

    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # 1. 把list 转成 hash表
        word_set = set(wordList)
        if len(word_set) == 0 or endWord not in word_set:
            return 0
        # 2.广度优先算法需要一个队列和一个访问的hash表,且起始的扩展为1
        queue = deque()
        queue.append(beginWord)
        visits = set(beginWord)
        step = 1
        if beginWord in word_set:
            word_set.remove(beginWord)
        # 3.循环遍历队列，取出每个单词，在每个位置上用a-z替字母
        while queue:
            queue_size = len(queue)
            for i in range(queue_size):
                cur_word = queue.popleft()
                chars = list(cur_word)
                n = len(chars)
                for j in range(n):
                    original_char = chars[j]
                    for k in range(26):
                        cur_char = chr(ord('a') + k)
                        if original_char == cur_char:
                            continue
                        chars[j] = cur_char
                        next_word = ''.join(chars)
                        if next_word in word_set:
                            if next_word == endWord:
                                return step + 1
                            if next_word not in visits:
                                queue.append(next_word)
                                visits.add(next_word)
                        chars[j] = original_char
            step += 1
        return 0


if __name__ == '__main__':
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot", "dot", "dog", "lot", "log"]
    solution = Solution()
    res = solution.ladderLength(beginWord, endWord, wordList)
    print(res)
    wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
    res = solution.ladderLength(beginWord, endWord, wordList)
    print(res)
