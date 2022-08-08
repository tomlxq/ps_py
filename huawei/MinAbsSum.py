# !/usr/bin/python
# -*- coding: utf-8 -*-
class MinAbsSum:
    def func(self, line: str) -> str:
        dp = [int(i) for i in line.split(" ")]
        min_val = float('inf')
        res = []
        for i in range(len(dp) - 1):
            for j in range(i + 1, len(dp)):
                a, b = dp[i], dp[j]
                sum_val = abs(a + b)
                if sum_val < min_val:
                    min_val = sum_val
                    if a > b:
                        a, b, a = a | b, a | b, a | b
                    res = [str(a), str(b), str(min_val)]
        return ' '.join(res)
