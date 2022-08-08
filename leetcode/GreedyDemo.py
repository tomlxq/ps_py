from typing import List, Optional
from collections import deque


class GreedyDemo:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        if not nums or len(nums) == 0:
            return 0
        if len(nums) == 1:
            return 1
        start, max_val = 0, 0
        for i in range(1, len(nums)):
            if nums[i] <= nums[i - 1]:
                start = i
            max_val = max(max_val, i - start + 1)
        return max_val

    def lemonadeChange(self, bills: List[int]) -> bool:
        five, ten = 0, 0
        for i in range(len(bills)):
            if bills[i] == 5:
                five += 1
            if bills[i] == 10:
                if five > 0:
                    five, ten = five - 1, ten + 1
                else:
                    return False
            if bills[i] == 20:
                if five > 0 and ten > 0:
                    five, ten = five - 1, ten - 1
                elif five >= 3:
                    five -= 3
                else:
                    return False
        return True

    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        for i in reversed(range(2, len(nums))):
            if nums[i] < nums[i - 1] + nums[i - 2]:
                return nums[i] + nums[i - 1] + nums[i - 2]
        return 0
