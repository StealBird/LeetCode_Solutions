# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        dummy = ListNode(0, head)
        slow = fast = dummy

        # Move fast n steps ahead
        for _ in range(n):
            fast = fast.next

        # Move both pointers until fast reaches the last node
        while fast.next:
            slow = slow.next
            fast = fast.next

        # Delete the nth node from the end
        slow.next = slow.next.next

        return dummy.next
        