"""
Linked list data structure.
"""
from __future__ import annotations
from typing import Optional, Sequence


def create(sequence: Optional[Sequence]) -> ListNode:
    """
    Create a linked list from a sequence and return the head node
    """
    head = ListNode()
    node = head
    tail = head
    for item in sequence:
        node.val = item
        node.next = ListNode()
        tail = node
        node = node.next
    tail.next = None
    return head


class ListNode:
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
