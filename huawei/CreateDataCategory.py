while 1:
    try:
        c, b, *nums = list(map(int, input().split()))

        dp = {}
        for a in nums:
            # 转16进制
            a_ = hex(a)[2:].zfill(8)
            temp = 0
            # 拆分
            for i in range(0, len(a_), 2):
                temp += int(a_[i: i+2], 16)

            # 取模
            t = temp % b
            if t < c:
                # 分类
                if t in dp:
                    dp[t] += 1
                else:
                    dp[t] = 1

        if dp:
            print(max(dp.values()))
        else:
            print(0)
    except Exception as e:
        break
