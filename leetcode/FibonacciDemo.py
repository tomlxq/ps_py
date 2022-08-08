from typing import List, Optional
from collections import deque


class FibonacciDemo:
    def fibonacci(self, n: int) -> int:
        def fb(num: int) -> int:
            if num <= 1:
                return num
            return fb(num - 1) + fb(num - 2)

        return fb(n)

    def fibonacci5(self, n: int) -> int:
        notebook = dict()

        def fb(num: int) -> int:
            if num <= 1:
                return num
            if num in notebook:
                return notebook[num]
            notebook[num] = fb(num - 1) + fb(num - 2)
            return notebook[num]

        return fb(n)

    def fibonacci2(self, n: int) -> int:
        mem = [-1] * (n + 1)

        def dbf(num: int) -> int:
            if num <= 1:
                return num
            if mem[num] != -1:
                return mem[num]
            left = dbf(num - 1)
            right = dbf(num - 2)

            mem[num] = (left + right) % 1000000007
            return mem[num]

        return dbf(n)

    def fibonacci3(self, n: int) -> int:
        if n <= 1:
            return n
        dp = [-1] * (n + 1)
        dp[0], dp[1] = 0, 1
        for i in range(2, n + 1):
            dp[i] = (dp[i - 1] + dp[i - 2]) % 1000000007
        return dp[n]

    def fibonacci4(self, n: int) -> int:
        if n <= 1:
            return n
        prev, curr = 0, 1
        for i in range(2, n + 1):
            total = (prev + curr) % 1000000007
            prev, curr = curr, total
        return curr

    def fibonacci6(self, n: int) -> int:
        if n <= 1:
            return n
        dp = {0: 0, 1: 1}
        for i in range(2, n + 1):
            dp[i] = (dp[i - 1] + dp[i - 2]) % 1000000007
        return dp[n]
