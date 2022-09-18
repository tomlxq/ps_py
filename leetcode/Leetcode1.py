from typing import List


class Leetcode1:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []

    def twoSum2(self, nums: List[int], target: int) -> List[int]:
        sign_map = {}
        for i in range(len(nums)):
            if target - nums[i] in sign_map:
                return [sign_map.get(target - nums[i]), i]
            else:
                sign_map[nums[i]] = i
        return []

    def twoSum3(self, numbers: List[int], target: int) -> List[int]:
        if not numbers or len(numbers) <= 1:
            return []
        n = len(numbers)
        for i in range(n):
            low, high = i, n - 1
            while low <= high:
                mid = low + (high - low >> 1)
                if numbers[mid] == target - numbers[i]:
                    if mid == i:
                        return [i + 1, mid + 2]
                    return [i + 1, mid + 1]
                elif numbers[mid] > target - numbers[i]:
                    high = mid - 1
                else:
                    low = mid + 1
        return []

    def twoSum4(self, numbers: List[int], target: int) -> List[int]:
        if not numbers or len(numbers) <= 1:
            return []
        l, r = 0, len(numbers)-1
        while l < r:
            sum = numbers[l] + numbers[r]
            if sum == target:
                return [l + 1, r + 1]
            elif sum > target:
                r -= 1
            else:
                l += 1
        return []