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


def are_equal(left: ListNode, right: ListNode) -> bool:
    """
    Test equality between the left and right linked lists with `left` and `right` head nodes
    """
    left_node = left
    right_node = right
    while True:
        if left_node.val != right_node.val:
            return False
        if left_node.next is None:
            if right_node.next is not None:
                return False
            else:
                break
        if right_node.next is None:
            if left_node.next is not None:
                return False
            else:
                break
        left_node = left_node.next
        right_node = right_node.next
    return True


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
