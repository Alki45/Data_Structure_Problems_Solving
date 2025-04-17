# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow,fast=head,head

        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        
        previous=None
        while slow:
            new_node=slow.next
            slow.next=previous
            previous=slow
            slow=new_node
    
        max_twin=0
        first=head
        second=previous
        while second:
            max_twin=max(max_twin,first.val+second.val)
            first=first.next
            second=second.next
        
        print(second)
        return max_twin
