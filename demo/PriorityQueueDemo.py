#coding:utf8
import heapq
from queue import Queue,PriorityQueue

# 使用heapq实现优先队列
# 定义一个可比较对象
class CompareAble:
    def __init__(self, priority, jobname):
        self.priority = priority
        self.jobname = jobname

    def __lt__(self, other):
        if self.priority < other.priority:
            return -1
        elif self.priority == other.priority:
            return 0
        else:
            return 1


pq = PriorityQueue()
pq.put(CompareAble(80, 'eat'))
pq.put(CompareAble(70, 'a write plan2'))
pq.put(CompareAble(70, 'write plan'))
pq.put(CompareAble(90, 'sleep'))
pq.put(CompareAble(100, 'write code'))

while pq.qsize() != 0:
    task = pq.get_nowait()
    print(task.jobname, task.priority)
