class Leetcode70:
    def climbStairs(self, n: int) -> int:
        def stairs(i):
            if i <= 2:
                return i
            return stairs(i - 1) + stairs(i - 2)
        return stairs(n)

    def climbStairs2(self, n: int) -> int:
        if n <= 2:
            return n
        dp = [0 for _ in range(n)]
        dp[0], dp[1] = 1, 2
        for i in range(2, n):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n - 1]

    def climbStairs3(self, n: int) -> int:
        if n <= 2:
            return n
        prev, curr = 1, 2
        for i in range(2, n):
            total = prev + curr
            prev, curr = curr, total
        return curr
