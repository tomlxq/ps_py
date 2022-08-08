class ConcatWord:
    def func(self, idx: int, line: str) -> str:
        list1 = line.split(" ")
        dp = [list1.pop(idx)]
        while len(list1):
            cache = []
            for w in list1:
                # 当前单词的首字母==最后一个单词的尾字母
                if w[0] == dp[-1][-1]:
                    cache.append(w)
            if cache:
                # 符合条件的单词排序 最长的长度排最前面，其次按字母排序
                cache = sorted(cache, key=lambda x: (-len(x), x))
                dp.append(cache[0])
                list1.remove(cache[0])
            else:
                break
        return ''.join(dp)


while True:
    try:
        # "worddwordda", 0,6,"word dd da dc dword d"
        idx = int(input())
        num = int(input())
        ary = [input() for _ in range(num)]
        cw = ConcatWord()
        print(cw.func(idx, ' '.join(ary)))
    except Exception as e:
        break
