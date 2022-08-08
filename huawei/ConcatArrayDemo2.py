while 1:
    try:
        n = int(input())

        nums = [input().split(',') for _ in range(n-1)]

        dp = []
        i = 0
        while nums:
            if len(nums[i]) > n:
                temp = nums[i][:n]
                nums[i] = nums[i][n:]
            else:
                temp = nums[i]
                nums.pop(i)
            dp += temp
            i += 1

            if i >= len(nums):
                i = 0

        print(",".join(dp))
    except Exception as e:
        break
