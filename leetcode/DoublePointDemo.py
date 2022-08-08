from typing import List, Optional
from collections import deque


class DoublePointExample:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums or len(nums) == 0:
            return 0
        n = len(nums)
        slow = 0
        for fast in range(1, n):
            if nums[fast] != nums[slow]:
                slow += 1
                nums[slow] = nums[fast]
        return slow + 1

    def pivotIndex(self, nums: List[int]) -> int:
        if not nums or len(nums) == 0:
            return -1
        sum_total = sum(nums)
        total = 0
        for i in range(len(nums)):
            total += nums[i]
            if total == sum_total:
                return i
            sum_total -= nums[i]
        return -1

    def pivotIndex2(self, nums: List[int]) -> int:
        if not nums or len(nums) == 0:
            return -1
        sum_total = sum(nums)
        total = 0
        for i in range(len(nums)):
            if 2 * total + nums[i] == sum_total:
                return i
            total += nums[i]
        return -1

    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        for i in range(m, n + m):
            print(i - m)
            nums1[i] = nums2[i - m]
        nums1.sort()

    def merge2(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        new_ary = [-1] * m
        p1, p2, p = 0, 0, 0
        for i in range(m):
            new_ary[i] = nums1[i]
        while p1 < m and p2 < n:
            if new_ary[p1] > nums2[p2]:
                nums1[p] = nums2[p2]
                p, p2 = p + 1, p2 + 1
            else:
                nums1[p] = new_ary[p1]
                p, p1 = p + 1, p1 + 1
        while p1 < m:
            nums1[p] = new_ary[p1]
            p, p1 = p + 1, p1 + 1
        while p2 < n:
            nums1[p] = nums2[p2]
            p, p2 = p + 1, p2 + 1

    def merge3(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        p1, p2, p = m - 1, n - 1, m + n - 1
        while p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p, p1 = p - 1, p1 - 1
            else:
                nums1[p] = nums2[p2]
                p, p2 = p - 1, p2 - 1
        while p2 >= 0:
            nums1[p] = nums2[p2]
            p, p2 = p - 1, p2 - 1
