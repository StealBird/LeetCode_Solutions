# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        #Tortoise and Hare algorithm 
        #initialize a tortoise and hare
        fast = head
        slow = head


        while fast is not None and fast.next is not None:#hare should not go past None or should not be none 
            slow = slow.next
            fast = fast.next.next

            if slow == fast:#if hare and tortoise meet there is a loop done by hare 
                return True#we return true if there is a loop in existence
        
        return False#or no loop if they meet if LL is linear maybe?
        