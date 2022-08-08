class DelLetterGame:
    def fun(self, nums: str) -> int:
        i = 0
        while i < len(nums):
            if nums[i] * 2 in nums:
                nums = nums.replace(nums[i] * 2, "")
                i = max(0, i - 1)
            else:
                i += 1
        return len(nums)

    def fun2(self, ls: str) -> int:
        # 方法一：
        #ls = input()
        # 或者直接输入转成列表ls=list(str(input()))
        # 绝对不能input().split()，这样会把输入的字符串分割成一个整体
        new_ls = []
        for k in ls:
            if len(new_ls) > 0:
                if k == new_ls[-1]:
                    new_ls.pop()
                else:
                    new_ls.append(k)
            else:
                new_ls.append(k)
        return len(new_ls)

    def fun3(self, ls: str) -> int:

        # 方法二：
        #ls = input()
        new_ls = []
        for i in ls:
            if new_ls and new_ls[-1] == i:
                new_ls.pop()
            else:
                new_ls.append(i)
        return len(new_ls)


while True:
    try:
        dlg = DelLetterGame()
        print(dlg.fun(input()))
    except Exception as e:
        break
