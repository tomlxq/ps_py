from collections import deque


class FindMinNum:
    def func(self, line: str, k: int) -> str:
        queue = deque()
        for digit in line:
            while queue and k > 0:
                c = queue.pop()
                if c < digit:
                    queue.append(c)
                    break
                else:
                    k -= 1
            queue.append(digit)
        for i in range(k):
            queue.popleft()
        res = []
        lead_zero = True
        while queue:
            c = queue.popleft()
            if c == '0' and lead_zero:
                if not queue:
                    res.append(c)
                continue
            lead_zero = False
            res.append(c)
        return ''.join(res)



