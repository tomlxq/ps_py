from typing import List, Optional
from collections import deque


class BfDemo:
    def findTheCity2(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        dis = [[float('inf') for _ in range(n)] for _ in range(n)]
        for i in range(n):
            dis[i][i] = 0
        for i, j, w in edges:
            dis[i][j] = w
            dis[j][i] = w
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    dis[i][j] = min(dis[i][j], dis[i][k] + dis[k][j])
        res, count = 0, n + 1
        for i in range(n):
            cur = 0
            for j in range(n):
                if dis[i][j] <= distanceThreshold:
                    cur += 1
            if cur <= count:
                res, count = i, cur
        return res

    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        # inf代表无穷大（infinity的缩写
        # 1.将无向图及权值转成二维数组存储，其中初始化任何两个点值为float('inf')无限大，而点自身到自身权值为0
        graph = [[float('inf') for _ in range(n)] for _ in range(n)]
        for i in range(n):
            graph[i][i] = 0
        # 2.实际输入的城市进行无向权值赋值
        for i, j, w in edges:
            graph[i][j], graph[j][i] = w, w
        # 3.用Floyed求，三重循环后,取两点之间的权限与通过第三点间接到距离，取最小值，即最短路径
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if i == j or graph[i][k] == float('inf') or graph[k][j] == float('inf'):
                        continue
                    graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
        # 4.循环遍历二维数组
        # ①统计某一顶点，当最短路径小于某一阀值，记录城市个数加和
        # ②然后与其它顶点的城市个数比较，若城市个数更小值更新，并更新其顶点值
        ret, min_num = 0, n + 1
        for i in range(n):
            cnt = 0
            for j in range(n):
                if i != j and graph[i][j] <= distanceThreshold:
                    cnt += 1
            if cnt <= min_num:
                ret, min_num = i, cnt
        return ret

    def hasPath2(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        # 1.计算一下行和列，用于判断小球不要超过边界
        # 2.声明一个记录访问节点的hash表visited
        # 3.利用bfs算法，还需要一个队列，循环队列，每个节点按四个方走，至到遇到墙停止
        # 4.若无节点在访问visited中，则加入到队列和visited
        row, col = len(maze), len(maze[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        visited = set()

        def dfs(x: int, y: int) -> bool:
            visited.add((x, y))
            if [x, y] == destination:
                return True
            for cur in directions:
                move_i, move_j = x, y
                while col > (t1 := move_i + cur[0]) >= 0 and 0 <= (t2 := move_j + cur[1]) < row and maze[t1][
                    t2] == 0:
                    move_i, move_j = t1, t2
                if move_i == x and move_j == y:
                    continue
                if (move_i, move_j) not in visited:
                    visited.add((move_i, move_j))
                    if dfs(move_i, move_j):
                        return True
            return False

        return dfs(start[0], start[1])

    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        # 1.计算一下行和列，用于判断小球不要超过边界
        # 2.声明一个记录访问节点的hash表visited
        # 3.利用bfs算法，还需要一个队列，循环队列，每个节点按四个方走，至到遇到墙停止
        # 4.若无节点在访问visited中，则加入到队列和visited
        row, col = len(maze), len(maze[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        visited = set()

        def bfs(x: int, y: int) -> bool:
            visited.add((x, y))
            queue = deque()
            queue.append([x, y])
            while queue:
                size = len(queue)
                for k in range(size):
                    [i, j] = queue.pop()
                    if [i, j] == destination:
                        return True
                    for cur in directions:
                        move_i, move_j = i, j
                        while col > (t1 := move_i + cur[0]) >= 0 and 0 <= (t2 := move_j + cur[1]) < row and maze[t1][
                            t2] == 0:
                            move_i, move_j = t1, t2
                        if move_i == i and move_j == j:
                            continue
                        if (move_i, move_j) not in visited:
                            visited.add((move_i, move_j))
                            queue.appendleft([move_i, move_j])
            return False

        return bfs(start[0], start[1])

    def ladder_length2(self, begin_word: str, end_word: str, word_list: List[str]) -> int:
        # 1.word_list放到hash表，并判断是否为空，是否包括了end_word
        # 2.双向广度优先需要两个hash begin_set,end_set列用于存放两端向中间扩散的集合，还要一个hash visited用于存放访问节点
        # 3.初始化路径为1
        # 4.判断两个begin_set,end_set不为空
        # ①比较大小，用小范围的来做下一轮的扩散，新增加一个next_visit_level用存储新的访问hash
        # ②循环遍历begin_set 取出每个单词后，对每个位置用26个字母替换后next_word
        # ③判断next_word是否在 word_list存在，若存在于end_set，直接返回step+1
        # ④判断在visited不存在，则执行加入到visited,并加到next_visit_level
        # ⑤将next_visit_level给begin_set，step+1，开始新一轮的扩散处理
        word_set = set(word_list)
        if len(word_set) == 0 or end_word not in word_set:
            return 0
        if begin_word in word_set:
            word_set.remove(begin_word)
        visited = set()
        visited.add(begin_word)
        visited.add(end_word)
        begin_set = set()
        begin_set.add(begin_word)
        end_set = set()
        end_set.add(end_word)
        step = 1
        word_size = len(end_word)
        while begin_set and end_set:
            if len(begin_set) > len(end_set):
                begin_set, end_set = end_set, begin_set
            next_visit_level = set()
            for word in begin_set:
                chars = list(word)
                for j in range(word_size):
                    original_char = chars[j]
                    for k in range(26):
                        cur_char = chr(ord('a') + k)
                        if cur_char == original_char:
                            continue
                        chars[j] = cur_char
                        next_word = ''.join(chars)
                        if next_word in word_set:
                            if next_word in end_set:
                                return step + 1
                            if next_word not in visited:
                                visited.add(next_word)
                                next_visit_level.add(next_word)
                    chars[j] = original_char
            step += 1
            begin_set = next_visit_level
        return 0

    def ladder_length(self, begin_word: str, end_word: str, word_list: List[str]) -> int:
        # 1.将单词列表放在hash表中，并判断是否为空，是否包括end_word
        # 2.广度优先需要1个队列，用以存储传播的节点，另一个用以存储访问节点
        # 3.处理逻辑 循环队列，取出每个单词，每个单词的位置与a-z替换，形成新的单词
        # 4.判断新的单词在word_set，判断是end_word，返回step+1
        # 3.判断新的单词在word_set，不在访问列表，则加入队列，并标记为已访问
        word_set = list(word_list)
        if len(word_set) == 0 or end_word not in word_set:
            return 0
        queue = deque()
        queue.append(begin_word)
        visited = set()
        visited.add(begin_word)
        step = 1
        word_len = len(end_word)
        while queue:
            size = len(queue)
            for k in range(size):
                cur_word = queue.popleft()
                chars = list(cur_word)
                for j in range(word_len):
                    original_char = chars[j]
                    for i in range(26):
                        cur_char = chr(ord('a') + i)
                        if cur_char == original_char:
                            continue
                        chars[j] = cur_char
                        next_word = ''.join(chars)
                        if next_word in word_set:
                            if next_word == end_word:
                                return step + 1
                            if next_word not in visited:
                                visited.add(next_word)
                                queue.append(next_word)
                    chars[j] = original_char
            step += 1
        return 0

    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        size, cnt = len(rooms), 0
        visited = {0}
        queue = deque([0])
        while queue:
            cnt += 1
            room_id = queue.popleft()
            for room in rooms[room_id]:
                if room not in visited:
                    visited.add(room)
                    queue.append(room)
        return size == cnt

    def canVisitAllRooms2(self, rooms: List[List[int]]) -> bool:
        size, cnt = len(rooms), 0
        visited = {0}

        def bfs(start) -> int:
            nonlocal cnt
            cnt += 1
            for room in rooms[start]:
                if room not in visited:
                    visited.add(room)
                    bfs(room)

        bfs(0)
        return size == cnt

    def minimumMoves(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        visit = set()
        target_x, target_y = m * n - 2, m * n - 1
        stack = deque()
        start, end = 0, 0
        stack.append([0, 1, 0])

        def check(x, y, step) -> bool:
            if x == target_x and y == target_y:
                return True
            if (x, y) in visit:
                return False
            visit.add((x, y))
            nonlocal end
            end += 1
            stack.append([x, y, step + 1])
            return False

        while start <= end:
            tmp = stack.popleft()
            a, b, step = tmp[0], tmp[1], tmp[2]
            start += 1
            x0, y0 = int(a / n), a % n
            x1, y1 = int(b / n), b % n
            # 向右
            if y0 + 1 < n and grid[x0][y0 + 1] == 0 and y1 + 1 < n and grid[x1][y1 + 1] == 0:
                if check(n * x0 + y0 + 1, n * x1 + y1 + 1, step):
                    return step + 1
                if y0 == y1:  # 竖直状态
                    if check(a, n * x0 + y0 + 1, step):
                        return step + 1
            # 向下
            if x0 + 1 < m and grid[x0 + 1][y0] == 0 and x1 + 1 < m and grid[x1 + 1][y1] == 0:
                if check(n * x0 + y0 + n, n * x1 + y1 + n, step):
                    return step + 1
                if x0 == x1:  # 水平状态
                    if check(a, n * x0 + y0 + n, step):
                        return step + 1
        return -1

    def minPathSum(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        row, col = len(grid), len(grid[0])
        # dp = [[float('inf') for _ in range(col)] for _ in range(row)]
        dp = [[0] * col for _ in range[row]]
        dp[0][0] = grid[0][0]
        for i in range(1, row):
            dp[i][0] = dp[i - 1][0] + grid[i][0]
        for i in range(1, col):
            dp[0][i] = dp[0][i - 1] + grid[0][i]
        for i in range(1, row):
            for j in range(1, col):
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]
        return dp[row - 1][col - 1]



    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1 for _ in range(n)] for _ in range(m)]
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[m - 1][n - 1]

    def uniquePaths2(self, m: int, n: int) -> int:
        dp = [1 for _ in range(n)]
        for i in range(1, m):
            for j in range(1, n):
                dp[j] = dp[j - 1] + dp[j]
        return dp[n - 1]

    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        temp = [[0] * n for _ in range(m)]
        for j in range(n):
            if obstacleGrid[0][j] == 0:
                temp[0][j] = 1
            else:
                break
        for i in range(m):
            if obstacleGrid[i][0] == 0:
                temp[i][0] = 1
            else:
                break

        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 0:
                    temp[i][j] = temp[i - 1][j] + temp[i][j - 1]
        return temp[-1][-1]

    def uniquePathsWithObstacles2(self, obstacleGrid: List[List[int]]) -> int:
        if not obstacleGrid:
            return 0
        row, col = len(obstacleGrid), len(obstacleGrid[0])
        dp = [0] * col
        dp[0] = 1 if obstacleGrid[0][0] == 0 else 0
        for i in range(row):
            for j in range(col):
                dp[j] = 0 if obstacleGrid[i][j] == 1 else dp[j] + dp[j - 1] if j > 0 else dp[j]
        return dp[-1]

    def insertSort(self, ary: List[int]):
        if not ary or len(ary) == 0:
            return
        size = len(ary)
        for i in range(1, size):
            j = i - 1
            while j >= 0:
                if ary[j] > ary[j + 1]:
                    ary[j], ary[j + 1] = ary[j + 1], ary[j]
                j -= 1

    def selectSort(self, ary: List[int]):
        if not ary or len(ary) == 0:
            return
        size = len(ary)
        for i in range(size):
            idx = i
            for j in range(i + 1, size):
                if ary[j] < ary[idx]:
                    idx = j
            ary[idx], ary[i] = ary[i], ary[idx]

    def bubbleSort(self, ary: List[int]):
        if not ary or len(ary) == 0:
            return
        size = len(ary)
        for i in reversed(range(size)):
            j = 0
            while j < i:
                if ary[j] > ary[j + 1]:
                    ary[j], ary[j + 1] = ary[j + 1], ary[j]
                j += 1
