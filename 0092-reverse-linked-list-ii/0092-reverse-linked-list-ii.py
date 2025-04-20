# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy=ListNode(0)
        dummy.next=head
        current=dummy
        for _ in range(left-1):
            current=current.next
        revrese=None
        current_loc=current.next
        for _ in range(right-left+1):
            new_node=current_loc.next
            current_loc.next=revrese
            revrese=current_loc
            current_loc=new_node
        current.next.next=current_loc
        current.next=revrese
        return dummy.next

        