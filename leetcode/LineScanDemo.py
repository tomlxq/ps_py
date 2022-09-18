from typing import List, Optional
from collections import deque


class LineScanDemo:
    def maximumProduct(self, nums: List[int]) -> int:
        if not nums or len(nums) < 3:
            return 0
        n = len(nums)
        nums.sort()
        return max(nums[0] * nums[1] * nums[n - 1], nums[n - 1] * nums[n - 2] * nums[n - 3])

    def maximumProduct2(self, nums: List[int]) -> int:
        if not nums or len(nums) < 3:
            return 0
        min1, min2, max1, max2, max3 = float('inf'), float('inf'), -float('inf'), -float('inf'), -float('inf')
        for x in nums:
            if x < min1:
                min2, min1 = min1, x
            elif x < min2:
                min2 = x
            if x > max1:
                max3, max2, max1 = max2, max1, x
            elif x > max2:
                max3, max2 = max2, x
            elif x > max3:
                max3 = x
        return max(min1 * min2 * max1, max1 * max2 * max3)


