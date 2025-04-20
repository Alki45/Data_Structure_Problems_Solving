# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        dummy=ListNode(0)
        preserve_dummy=ListNode(0)
        preserve_less=preserve_dummy
        greater=dummy
        current=head
        while current:
            if current.val < x :
                preserve_less.next = current
                preserve_less = preserve_less.next    

            else:
                greater.next = current
                greater=greater.next

            current=current.next

        greater.next = None
        preserve_less.next = dummy.next
        return preserve_dummy.next


        