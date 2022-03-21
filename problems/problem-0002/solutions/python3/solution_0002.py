"""
solution_0002.py
"""
from __future__ import annotations
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    @classmethod
    def from_list(cls: ListNode, l: list) -> ListNode:
        ln = ListNode(l[0])
        _ln = ln
        for x in l[1:]:
            _ln.next = ListNode(x)
            _ln = _ln.next
        return ln
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __eq__(self, other) -> bool:
        self_ln = self
        other_ln = other
        while True:
            if self_ln.val != other_ln.val:
                return False
            if self_ln.next is None:
                if other_ln.next is not None:
                    return False
                else:
                    break
            if other_ln.next is None:
                if self_ln.next is not None:
                    return False
                else:
                    break
            self_ln = self_ln.next
            other_ln = other_ln.next
        return True


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
