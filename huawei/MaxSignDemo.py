class MaxSignDemo:
    def func(self, line: str) -> str:
        max_len = 0
        s = "-1"
        cache = []
        for c in line:
            if cache and cache[-1] == c == '0':
                line2 = ''.join(cache)
                if "11" not in line2:
                    max_len = max(max_len, len(line2))
                    if max_len == len(line2):
                        s = line2
                cache = [c]
            else:
                cache.append(c)
        return s


while True:
    try:
        msd = MaxSignDemo()
        print(msd.func(input()))
    except Exception as e:
        break
