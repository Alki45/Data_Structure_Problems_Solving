# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        previous=None
        current=head
        while current:
            new_node=current.next
            current.next=previous
            previous=current
            current=new_node
        return previous
        