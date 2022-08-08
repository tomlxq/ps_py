from collections import deque
from typing import List

from TreeNode import TreeNode


class DfsBfsDemo:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        if not root.left and not root.right:
            return 1
        deep_val = float('inf')
        if root.left:
            deep_val = min(deep_val, DfsBfsDemo.minDepth(self, root.left))
        if root.right:
            deep_val = min(deep_val, DfsBfsDemo.minDepth(self, root.right))
        return deep_val + 1

    def minDepth2(self, root: TreeNode) -> int:
        if not root:
            return 0
        queue = deque()
        queue.append(root)
        deep = 0
        while queue:
            size = len(queue)
            deep += 1
            for i in range(size):
                tmp = queue.popleft()
                if not tmp.left and not tmp.right:
                    return deep
                if tmp.left:
                    queue.append(tmp.left)
                if tmp.right:
                    queue.append(tmp.right)
        return 0

    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        cities = len(isConnected)
        visited = set()
        provinces = 0

        def dfs(i: int):
            for j in range(cities):
                if isConnected[i][j] == 1 and j not in visited:
                    visited.add(j)
                    dfs(j)

        for i in range(cities):
            if i not in visited:
                dfs(i)
                provinces += 1
        return provinces

    def findCircleNum2(self, isConnected: List[List[int]]) -> int:
        visited = set()
        cities = len(isConnected)
        queue = deque()
        provinces = 0
        for i in range(cities):
            queue.append(i)
            if i not in visited:
                while queue:
                    k = queue.popleft()
                    visited.add(k)
                    for j in range(cities):
                        if isConnected[k][j] == 1 and j not in visited:
                            queue.append(j)
                provinces += 1
        return provinces

    def findCircleNum3(self, isConnected: List[List[int]]) -> int:
        cities = len(isConnected)
        head = [i for i in range(cities)]
        level = [1] * cities
        def find(x: int):
            if x == head[x]:
                return x
            head[x] = find(head[x])
            return head[x]

        def merge(x: int, y: int):
            i = find(x)
            j = find(y)
            print(head)
            if i == j:
                return
            if level[i] <= level[j]:
                head[i] = j
            else:
                head[j] = i
            if level[i] == level[j]:
                level[i], level[j] = level[i] + 1, level[j] + 1

        for i in range(cities):
            for j in range(i + 1, cities):
                if isConnected[i][j] == 1:
                    merge(i, j)
        cnt = 0
        for i in range(cities):
            if i == head[i]:
                cnt += 1
        return cnt
