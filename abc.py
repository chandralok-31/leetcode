##########################1721

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        slow=head
        fast=head
        for i in range(k-1):
            fast=fast.next
        first=fast
        while fast!=None and fast.next!=None:
            fast=fast.next
            slow=slow.next
            
        second=slow
        
        first.val,second.val=second.val,first.val
        return head



############19

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fast=head
        slow=head
        for i in range(n):
            fast=fast.next
        if not fast:
            return head.next
        while fast.next:
            fast=fast.next
            slow=slow.next
        slow.next=slow.next.next
        return head




        
        
        
        
        
        
        
        
        
        
        
        
        
  
        