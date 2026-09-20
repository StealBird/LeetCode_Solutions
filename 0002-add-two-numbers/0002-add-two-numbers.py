# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        
        curr1 = l1
        curr2 = l2
        carry = 0
        dummy = ListNode(0)
        curr = dummy

        while curr1 or curr2 or carry:
            sum = 0
            if curr1 != None:
                sum += curr1.val
                curr1 = curr1.next
            
            if curr2 != None:
                sum += curr2.val
                curr2 = curr2.next

            sum += carry
            
            carry = sum//10
            digit = sum % 10

            curr.next = ListNode(digit)
            curr = curr.next
        
        return dummy.next

        
