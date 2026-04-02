# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        before = ListNode(0)
        after = ListNode(0)
        before_list = before
        after_list = after
        current = head
        while current:
            if current.val < x:
                before_list.next = current
                before_list = before_list.next
            else:
                after_list.next = current
                after_list = after_list.next
            current = current.next
        after_list.next = None
        before_list .next = after.next
        return before.next
