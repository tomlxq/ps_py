class ArrayUniqueOrder:
    def func(self, line: str) -> str:
        ary = line.split(',')
        res_map = {}
        for c in ary:
            if res_map.get(c):
                res_map[c] = res_map.get(c) + 1
            else:
                res_map[c] = 1
        # res_map.items()取出键和值
        res_map = sorted(res_map.items(), key=lambda x: x[1], reverse=True)
        # 取出键形成列表
        res = [i[0] for i in res_map]
        return ','.join(res)


while True:
    try:
        auo = ArrayUniqueOrder()
        print(auo.func(input()))
    except Exception as e:
        break
