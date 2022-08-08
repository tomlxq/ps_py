from typing import List


class RecursiveDemo:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        def max_score(l: int, r: int) -> int:
            if l == r:
                return nums[l]
            lsum, rsum = 0, 0
            if r - l == 1:
                lsum = nums[l]
                rsum = nums[r]
            if r - l > 1:
                lsum += nums[l] + min(max_score(l + 1, r - 1), max_score(l + 2, r))
                rsum += nums[r] + min(max_score(l + 1, r - 1), max_score(l, r - 2))
            return max(lsum, rsum)

        size = len(nums)
        total = 0
        for i in range(size):
            total += nums[i]
        l, r = 0, size - 1
        play1 = max_score(l, r)
        if play1 >= total - play1:
            return True
        else:
            return False

    def PredictTheWinner4(self, nums: List[int]) -> bool:
        length = len(nums)
        if length % 2 == 0:
            return True
        dp = [nums[i] for i in range(length)]
        for l in reversed(range(length - 1)):
            for r in range(l + 1, length):
                dp[r] = max(nums[l] - dp[r], nums[r] - dp[r - 1])
        if dp[length - 1] >= 0:
            return True
        else:
            return False
