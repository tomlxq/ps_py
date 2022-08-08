class MiniAbsArray:
    def func(self, line: str) -> str:
        a_list = list(map(int, line.split(" ")))
        size = len(a_list)
        min_val = float('inf')
        res = []
        for i in range(size):
            for j in range(i + 1, size - 1):
                tmp_sum = abs(a_list[i] + a_list[j])
                min_val = min(tmp_sum, min_val)
                if tmp_sum == min_val:
                    res = [str(a_list[i]), str(a_list[j]), str(min_val)]
        return ' '.join(res)


while True:
    try:
        maa = MiniAbsArray()
        print(maa.func(input()))
    except Exception as e:
        break

