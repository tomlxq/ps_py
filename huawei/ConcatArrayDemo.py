from typing import List


class ConcatArrayDemo:
    def func(self, lines: List[str], max_len: int) -> str:
        ary_list = []
        for line in lines:
            ary_list.append(line.split(","))
        res = []
        count = 0
        while count < len(ary_list):
            for line in ary_list:
                if len(line) >= max_len:
                    for j in range(max_len):
                        res.append(line.pop(0))
                elif 0 < len(line) < max_len:
                    for i in range(len(line)):
                        res.append(line.pop(0))
                else:
                    count += 1
        return ','.join(res)


while True:
    try:
        c = int(input())
        n = int(input())
        a_list = []
        for i in range(n):
            a_list.append(input())
        cad = ConcatArrayDemo()
        print(cad.func(a_list, c))
    except Exception as e:
        break
