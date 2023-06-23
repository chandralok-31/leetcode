# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow,fast=head,head
        maxval=0
        while fast and fast.next:
            fast=fast.next.next
            slow=slow.next
            
        cur=slow
        prev=None
        while cur:
            tem=cur.next
            cur.next=prev
            prev=cur
            cur=tem
            
        while prev:
            maxval=max(maxval,head.val+prev.val)
            prev=prev.next
            head=head.next

        return maxval


            
        
               
        
        
        
#         temp=head
#         arr=[]
#         while temp:
#             arr.append(temp.val)
#             temp=temp.next
#         n=len(arr)
#         x=n//2-1
#         sm=0
#         for  i in range(x+1):
            
#             sm=max(sm,(arr[i]+arr[n-1-i]))
#         return sm
            
        
        