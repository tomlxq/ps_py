class CreateDataCategory:
    def func(self, line: str) -> int:
        c, b, *nums = list(map(int, line.split()))
        dp = {}
        for num in nums:
            # 转16进制
            tmp = hex(num)[2:].zfill(8)
            sum_val = 0
            for i in range(0, len(tmp), 2):
                sum_val += int(tmp[i:i + 2], 16)
            # 取模
            t = sum_val % b
            if t < c:
                # 分类
                if t in dp:
                    dp[t] += 1
                else:
                    dp[t] = 1
        if dp:
            return max(dp.values())
        else:
            return 0


while 1:
    try:
        cdc = CreateDataCategory()
        print(cdc.func(input()))
    except Exception as e:
        break