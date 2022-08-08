# !/usr/bin/python
# -*- coding: utf-8 -*-
class MiniStopBus:
    def func(self, line: str) -> int:
        s = ''.join(i for i in line.split(',')).replace('111', '3').replace('11', '2')
        return s.count('1') + s.count('2') + s.count('3')

    def func2(self, line: str) -> int:
        list_a = ''.join(i for i in line.split(',')).split('0')
        total = 0
        for line in list_a:
            size = len(line)
            big = int(size / 3)
            mid = int((size - big * 3) / 2)
            small = size - big * 3 - mid * 2
            total += big + mid + small
        return total


cars = ("".join(i for i in (input().split(",")))).split("0")  ##通过0分割成若干个1的列表
# print(cars)
num = 0  ##定义累加器
for i in cars:
    lennum = (len(i))  ##判断1的长度
    if lennum == 0:
        num = num
    elif not lennum % 3 and len != 0:  ##%取余
        num = num + lennum / 3
    elif lennum % 3:
        num = num + (lennum - lennum % 3) / 3 + 1
print(int(num))
