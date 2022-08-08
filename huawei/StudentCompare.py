class StudentCompare:
    def compare(self, line1: str, line2: str) -> str:
        h, m = map(int, line1.split())
        nums = list(map(int, line2.split()))
        nums = sorted(nums, key=lambda x: (abs(x - h), x))
        # for i in nums:
        #    print(i, end=" ")
        return " ".join(map(str, nums))


if __name__ == '__main__':
    so = StudentCompare()
    # so.input_data(deBug=False)
    # 100 10
    # 95 96 97 98 99 101 102 103 104 105
    while True:
        try:
            s = so.compare(input(), input())
            print(s)
        except:
            break
