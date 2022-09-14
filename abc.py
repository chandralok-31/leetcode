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




        
        
############24        
        
        
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow=head
        
        if not head or not head.next:
            return head
        fast=head.next
        while fast!=None :
            first=slow
            second=fast
            first.val,second.val=second.val,first.val
            slow=slow.next.next
            fast=fast.next
            if fast!=None:
                fast=fast.next
            else:
                return head
        return head      
        
        
        




############# 141        
        
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow=head
        fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
            
            if slow==fast:
                return True
        return False    
        
  
        

#############  125
class Solution:
    def isPalindrome(self, s: str) -> bool:
        t = ""
        la="abcdefghijklmnopqrstuvwxyz"
        ua="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        n="0123456789"
        for i in s:
            if(i in la or i in ua or i in n):
                t+=i
        
        t=t.lower()
        print(t)
        if t==t[::-1]:
            return True
        return False
