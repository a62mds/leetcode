"""
solution_0002.py
"""
from typing import Optional

from linkedlist import ListNode


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result: ListNode = ListNode()
        current: ListNode = result
        p: Optional[ListNode] = l1
        q: Optional[ListNode] = l2
        carry: int = 0
        while p or q:
            sum: int = (p.val if p else 0) + (q.val if q else 0) + carry
            carry = sum // 10
            sum = sum % 10
            current.next = ListNode(sum)
            current = current.next
            if p:
                p = p.next
            if q:
                q = q.next
        if carry:
            current.next = ListNode(carry)
        return result.next
