class CalMinSumDemo:
    def func(self, line1: str, line2: str, count: int) -> int:
        ary1 = list(map(int, line1.split(" ")))
        ary2 = list(map(int, line2.split(" ")))
        dp = []
        for c1 in ary1:
            for c2 in ary2:
                dp.append(c1 + c2)
        dp.sort()
        return sum(dp[:count])


while 1:
    try:
        csd = CalMinSumDemo()
        print(csd.func(input(), input(), int(input())))
    except Exception as e:
        break
