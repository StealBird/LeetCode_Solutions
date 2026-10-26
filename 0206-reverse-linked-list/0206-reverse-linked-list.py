# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        prev = None
        curr = head

        while curr:
            nxt = curr.next    # save the rest of the list
            curr.next = prev   # flip the pointer
            prev = curr        # move prev forward
            curr = nxt         # move curr forward

        return prev            # prev is the new head
        