class PythagoreanDemo:
    def func(self, n: int, m: int) -> str:

        def ac(a: int, b: int) -> int:
            mod = 2
            while mod != 0:
                mod = a % b
                a, b = b, mod
            return a

        res = []
        for i in range(n, m + 1):
            for j in range(i + 1, m + 1):
                for k in range(j + 1, m + 1):
                    if i * i + j * j == k * k and ac(i, j) == ac(j, k) == ac(i, k) == 1:
                        res.append("%d %d %d" % (i, j, k))
        if len(res) == 0:
            return 'Na'
        return '\n'.join(res)
