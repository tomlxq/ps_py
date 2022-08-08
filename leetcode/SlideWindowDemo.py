from typing import Optional, List, Set
from ListNode import ListNode
from collections import deque


class SlideWindowDemo:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        if not nums or len(nums) == 0:
            return 0
        total = 0
        for i in range(k):
            total += nums[i]
        max_val = total
        n = len(nums)
        for i in range(k, n):
            total = total - nums[i - k] + nums[i]
            max_val = max(total, max_val)
        return max_val * 1.0 / k
