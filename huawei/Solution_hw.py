class Solution_hw(object):
    def __init__(self):
        super(Solution_hw, self).__init__()
        self.input_str = ""
        self.stack_l = []

    def input_data(self, deBug=False):
        if deBug:
            self.input_str = "(u(love)i)"

        else:

            try:
                self.input_str = input("please input str : ")
            except:
                pass

    def reverse_str(self):
        # [1] reverse
        input_str_list = list(self.input_str) # "abc" -> ['a', 'b', 'c']

        for idx in range(len(input_str_list)):
            # save '(' idx
            if input_str_list[idx] == '(':
                self.stack_l.append(idx)

            # pop '(' idx
            if input_str_list[idx] == ')':
                l_idx = self.stack_l[-1]
                self.stack_l.pop()

                # reverse [l_idx,idx]
                input_str_list[l_idx+1:idx] = input_str_list[l_idx+1:idx][::-1]

        # [2] pop '(' & ')'
        out_str = ""
        for c in input_str_list:
            if c == '(' or c == ')':
                continue
            out_str += c

        return out_str

    def output_info(self):
        print(self.reverse_str())




if __name__ == '__main__':
    so = Solution_hw()
    so.input_data(deBug=False)
    so.output_info()