from typing import Optional, List, Set
from ListNode import ListNode
from collections import deque


class ListDemo:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        curr = head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev

    def reverseList2(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        new_node = self.reverseList2(head.next)
        head.next.next = head
        head.next = None
        return new_node

    def hasCycle(self, head: Optional[ListNode]) -> bool:
        data = []
        while head:
            if head in data:
                return True
            data.append(head)
            head = head.next
        return False

    def hasCycle2(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return False
        slow = head
        quick = head.next
        while slow != quick:
            if not quick or not quick.next:
                return False
            slow = slow.next
            quick = quick.next.next
        return True
