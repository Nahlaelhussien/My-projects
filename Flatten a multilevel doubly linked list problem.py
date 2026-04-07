
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return head
        current = head
        while current:
            if current.child:
                next_node=current.next
                child_head= current.child
                current.next = child_head
                child_head.prev=current
                current.child=None
                dummy=child_head
                while dummy.next:
                    dummy=dummy.next
                if next_node:
                    dummy.next=next_node
                    next_node.prev=dummy
            current=current.next
        return head
