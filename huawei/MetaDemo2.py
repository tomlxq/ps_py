def longest_alp(degree, string):
    ary_meta = tuple("aeiouAEIOU")
    head, length, tail = 0, 0, len(string) - 1

    def flaw_degree(string):
        degree = 0
        for i in string:
            if i in ary_meta:
                continue
            degree += 1
        return degree

    result = []
    while head <= tail:

        if string[head].startswith(ary_meta) and string[tail].endswith(ary_meta):
            result.append(string[head:tail + 1])
            if string[head + 1].startswith(ary_meta):
                tail -= 1
            else:
                head += 1
        elif string[head].startswith(ary_meta) and not string[tail].endswith(ary_meta):
            tail -= 1
        else:
            head += 1

    for item in result:
        if flaw_degree(item) == degree:
            length = max(length, len(item))
    return length


if __name__ == '__main__':
    print(longest_alp(0, "asdbuiodevauufgh"))
    print(longest_alp(2, "aeueo"))
    print(longest_alp(1, "aabeebuu"))