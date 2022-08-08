from typing import List, Optional
from collections import deque


class EratosthenesDemo:
    def countPrimes(self, n: int) -> int:
        def isPrime(num) -> bool:
            n = int(num ** 0.5 + 1)
            for j in range(2, n):
                if num % j == 0:
                    return False
            return True

        if n <= 1:
            return 0
        count = 0
        for i in range(2, n):
            if isPrime(i):
                count += 1
        return count

    def countPrimes2(self, n: int) -> int:
        prime = [False] * n
        count = 0
        for i in range(2, n):
            if not prime[i]:
                count += 1
                if i * i < n:
                    for j in range(i * i, n, i):
                        prime[j] = True
        return count
