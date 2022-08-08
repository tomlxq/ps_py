class StudentOrder:
    def func(self, n: int, high: str, weight: str) -> str:
        weight_ary = list(map(int, weight.split(" ")))
        high_ary = list(map(int, high.split(" ")))
        dp = []
        for i in range(n):
            dp.append((i + 1, high_ary[i], weight_ary[i]))
        dp = sorted(dp, key=lambda x: (x[1], x[2]))
        res = [str(i[0]) for i in dp]
        return ''.join(res)


while 1:
    try:
        lens = int(input())
        a = list(map(int, input().split()))
        b = list(map(int, input().split()))

        nums = []
        for i in range(1, lens + 1):
            nums.append((i, a[i - 1], b[i - 1]))

        nums = sorted(nums, key=lambda x: (x[1], x[2]))
        print(" ".join([str(i[0]) for i in nums]))
    except Exception as e:
        break
