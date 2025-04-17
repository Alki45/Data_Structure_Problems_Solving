# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry=0
        dummy=ListNode()
        Summ=dummy
        while l1 or l2 or carry:
            if l1:
                l1_num=l1.val
            else:
                l1_num=0
            if l2:
                l2_num=l2.val
            else:
                l2_num=0     
            summ = l1_num + l2_num + carry
            carry = summ//10
            Summ.next = ListNode( summ % 10 )
            Summ = Summ.next
            if l1:
                l1=l1.next
            if l2:
                l2=l2.next

        return dummy.next
        