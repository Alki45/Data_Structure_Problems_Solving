# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        length=0
        current=head
        while current:
            current=current.next
            length+=1
        
        dummy=ListNode(0)
        dummy.next=head
        current=dummy
        if length%2==0:
            for _ in range(length//2+1):
                current=current.next
        if length%2==1:
            for _ in range(length//2 +1):
                current=current.next
        return current

        