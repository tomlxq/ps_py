class ReverseEnglishClause:
    def func(self, line: str, begin_idx: int, end_idx: int) -> str:
        ary = list(map(str, line.split(" ")))
        if len(ary) == 1 or begin_idx >= len(ary):
            return "EMPTY"
        ary2 = list()
        i = 0
        while i < len(ary):
            if end_idx >= i >= begin_idx:
                for j in reversed(range(begin_idx, end_idx + 1)):
                    ary2.append(ary[j])
                i = end_idx + 1
            else:
                ary2.append(ary[i])
                i += 1
        return ' '.join(ary2)


while True:
    try:
        rec = ReverseEnglishClause()
        print(rec.func(input(), int(input()), int(input())))
    except Exception as e:
        break
