from typing import List, Optional
from collections import deque


class DpExample:
    def numSquares(self, n: int) -> int:
        dp = [0 for _ in range(n + 1)]
        for i in range(1, n + 1):
            dp[i] = i
            j = 1
            while i - j * j >= 0:
                dp[i] = min(dp[i], dp[i - j * j] + 1)
                j += 1

        return dp[n]

    def numSquares2(self, n: int) -> int:
        # 队列
        queue = deque()
        # 入队出队的节点
        queue.append((n, 0))
        # 已访问的集合
        visited = set()
        visited.add(n)
        while queue:
            # 操作队列 —— 弹出队首节点
            number, step = queue.popleft()
            # 操作弹出的节点 —— 根据业务生成子节点（一个或多个）
            targets = [number - i * i for i in range(1, int(number ** 0.5) + 1)]
            for target in targets:
                # 判断这些节点 —— 符合业务条件，则return
                if target == 0:
                    return step + 1
                # 不符合业务条件，且不在已访问集合，则追加到队尾，并加入已访问集合
                if target not in visited:
                    visited.add(target)
                    queue.append((target, step + 1))
        return -1

    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if not triangle or not triangle[0]:
            return -1
        if len(triangle) == 1:
            return triangle[0][0]
        h = len(triangle)
        dp = [[0 for _ in range(len(triangle[j]))] for j in range(h)]
        for i in reversed(range(h)):
            for j in range(len(triangle[i])):
                if i == h - 1:
                    dp[i][j] = triangle[i][j]
                else:
                    dp[i][j] = min(dp[i + 1][j], dp[i + 1][j + 1]) + triangle[i][j]
        return dp[0][0]

    def minimumTotal2(self, triangle: List[List[int]]) -> int:
        if not triangle or not triangle[0]:
            return -1
        if len(triangle) == 1:
            return triangle[0][0]
        h = len(triangle)
        dp = [0 for _ in range(h)]
        for i in reversed(range(h)):
            for j in range(len(triangle[i])):
                if i == h - 1:
                    dp[j] = triangle[i][j]
                else:
                    dp[j] = min(dp[j], dp[j + 1]) + triangle[i][j]
        return dp[0]

    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return -1
        pre_max = pre_min = res = nums[0]
        for i in range(1, len(nums)):
            if nums[i] < 0:
                pre_max, pre_min = pre_min, pre_max
            pre_max = max(pre_max * nums[i], nums[i])
            pre_min = min(pre_min * nums[i], nums[i])
            res = max(res, pre_max)
        return res

    def maxProfit(self, prices: List[int]) -> int:
        if not prices or len(prices) == 0:
            return 0
        n = len(prices)
        dp = [[[0] * 2 for _ in range(2)] for _ in range(n)]
        dp[0][1][0] = 0
        dp[0][1][1] = -prices[0]
        for i in range(1, n):
            dp[i][1][0] = max(dp[i - 1][1][0], dp[i - 1][1][1] + prices[i])
            dp[i][1][1] = max(dp[i - 1][1][1], dp[i - 1][0][0] - prices[i])
        return dp[n - 1][1][0]

    def maxProfit2(self, prices: List[int]) -> int:
        if not prices or len(prices) == 0:
            return 0
        n = len(prices)
        sell = 0
        buy = -prices[0]
        for i in range(1, n):
            sell = max(sell, buy + prices[i])
            buy = max(buy, 0 - prices[i])
        return sell

    def maxProfit122(self, prices: List[int]) -> int:
        if not prices or len(prices) == 0:
            return 0
        n = len(prices)
        dp = [[0] * 2 for _ in range(n)]
        dp[0][0] = 0
        dp[0][1] = -prices[0]
        for i in range(1, n):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - prices[i])
        return dp[n - 1][0]

    def maxProfit1222(self, prices: List[int]) -> int:
        if not prices or len(prices) == 0:
            return 0
        n = len(prices)
        sell = 0
        buy = -prices[0]
        for i in range(1, n):
            sell = max(sell, buy + prices[i])
            buy = max(buy, sell - prices[i])
        return sell
