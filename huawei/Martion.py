class Martion(object):
    def func2(self, nums: str) -> int:
        # 无符号数
        index_list = [i for i, c in enumerate(nums) if c in "#$"]

        # 按操作符 分隔字符串
        stack = []
        s = 0
        for e in index_list:
            stack.append(int(nums[s:e]))
            stack.append(nums[e])
            s = e + 1
        else:
            stack.append(int(nums[s:]))
        # 计算 优先级高的$ f"3*{x}+{y}+2")
        r_stack = []
        while stack:
            item = stack.pop()
            if item == "$":
                x = stack.pop()
                y = r_stack.pop()
                stack.append(eval(f"3*{x}+{y}+2"))
            else:
                r_stack.append(item)
        stack += r_stack[::-1]

        # 计算 2*{x}+3*{y}+4"
        x = stack[0]
        for i in range(2, len(stack), 2):
            y = stack[i]
            x = eval(f"2*{x}+3*{y}+4")
        return x

    def func(self, nums: str) -> int:
        '''x#y = 2x+3y+4
    x$y = 3*x+y+2
    $的优先级高于#'''

        def func3(nums: str) -> int:
            idx = nums.rfind("#")
            if idx != -1:
                left = nums[0:idx]
                right = nums[idx + 1:]
                return 2 * func3(left) + 3 * func3(right) + 4
            idx = nums.rfind("$")
            if idx != -1:
                left = nums[0:idx]
                right = nums[idx + 1:]
                return 3 * func3(left) + func3(right) + 2
            return int(nums)

        return func3(nums)


while 1:
    try:
        nums = input()
        m = Martion()
        print(m.func(nums))
    except Exception as e:
        break
