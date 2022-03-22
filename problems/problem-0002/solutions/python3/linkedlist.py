"""
Linked list data structure.
"""
from __future__ import annotations

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
