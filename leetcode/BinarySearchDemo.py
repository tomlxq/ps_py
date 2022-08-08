from typing import List, Optional
from collections import deque
import sys


class BinarySearchExample:
    def mySqrt(self, x: int) -> int:
        idx, l, r = -1, 0, x
        while l <= r:
            mid = l + (r - l >> 1)
            if mid * mid <= x:
                idx = mid
                l = mid + 1
            else:
                r = mid - 1
        return idx

    def mySqrt2(self, x: int) -> int:
        def sqrt(i):
            res = (i + x / i) / 2
            if res == i:
                return res
            return sqrt(res)

        if x == 0:
            return 0
        return int(sqrt(x))

    def arrangeCoins(self, n: int) -> int:
        for i in range(1, n):
            n -= i
            if i >= n:
                return i
        return n

    def arrangeCoins2(self, n: int) -> int:
        low, high = 0, n
        while low <= high:
            mid = low + (high - low >> 1)
            cost = (mid + 1) * mid / 2
            if cost == n:
                return mid
            elif cost < n:
                low = mid + 1
            else:
                high = mid - 1
        return high

    sys.setrecursionlimit(100000)

    # (x+n/x)/2=x*x  (x+1)*x/2=n
    def arrangeCoins3(self, n: int) -> int:
        def sqrt(x):
            res = (x + (2 * n - x) / x) / 2
            if res == x:
                return res
            return sqrt(res)

        if n == 0:
            return 0
        return int(sqrt(n))

    # x^2+x=2n ==> 4x^2+4x+1=8n+1
    def arrangeCoins4(self, n: int) -> float:
        return int((pow(8 * n + 1, 0.5) - 1) / 2)

    def arrangeCoins5(self, n: int) -> float:
        res = 0
        while res < n:
            res += 1
            n -= res
        return res
