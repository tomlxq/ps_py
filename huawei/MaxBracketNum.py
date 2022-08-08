class MaxBracketNum:
    def func(self, line: str) -> int:
        brackets = {"{": "}", "[": "]", "(": ")"}
        stacks_open = []
        stacks_close = []
        res = 0
        for c in line:
            if c in brackets.keys():
                stacks_open.append(c)
                stacks_close.append(brackets.get(c))
            else:
                if not stacks_open:
                    return res
                if c in brackets.values():
                    res = max(res, len(stacks_open))
                    c1 = stacks_open.pop()
                    c2 = stacks_close.pop()
                    if c != c2 or f"{c1}{c2}" not in ["[]", "{}", "()"]:
                        return 0
        else:
            if len(stacks_open) > 0:
                return 0
        return res


while 1:
    try:
        nums = input()
        max_ = 0
        stack = []
        for c in nums:
            if c in "{[(":
                stack.append(c)
            elif c in "]})":
                max_ = max(max_, len(stack))
                cr = stack.pop()
                if f"{cr}{c}" not in ["[]", "{}", "()"]:
                    max_ = 0
                    break
        else:  # break 不执行
            if len(stack) > 0:
                max_ = 0
        print(max_)
    except Exception as e:
        break
