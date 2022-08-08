class MetaDemo(object):
    def fun2(self, num: str, nums: str) -> int:
        bct = "aeiou"
        count, flaw, max_num = 0, int(num), 0
        for read in range(len(nums)):
            if nums[read] in bct:
                count += 1
            elif flaw > 0:
                count += 1
                flaw -= 1
            else:
                max_num = max(max_num, count)
                count = 0
        return max_num

    def fun(self, num: str, nums: str) -> int:
        bct = "aeiou"
        k = int(num)
        nums = nums

        n = len(nums)
        nums = [1 if c in bct else 0 for c in nums]
        # asdbuiodevauufgh
        # [1, 0, 0, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 0, 0]
        l = r = 0
        count = 0
        maxlen = 0
        while r < len(nums):
            if nums[r] == 0:
                count += 1
            while count > k:
                if nums[l] == 0:
                    count -= 1
                    l += 1
            if nums[l] == nums[r] == 1 and count == k:
                maxlen = max(r - l + 1, maxlen)
            r += 1
        return maxlen


while 1:
    try:
        md = MetaDemo()
        print(md.fun(input(), input()))
    except Exception as e:
        break
