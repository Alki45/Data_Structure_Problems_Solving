# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        length=1
        tail=head

        if not head or not head.next or k==0:
            return head
        while tail and tail.next:
            tail=tail.next
            length+=1

        k=k%length
        tail.next=head
        rotate=length-k

        rotation=head
        

        for _ in range(rotate-1):
            rotation = rotation.next
            
        current_head=rotation.next
        rotation.next=None

        return current_head
        