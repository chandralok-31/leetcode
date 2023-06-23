# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        temp=head
        arr=[]
        while temp:
            arr.append(temp.val)
            temp=temp.next
        n=len(arr)
        x=n//2-1
        sm=0
        for  i in range(x+1):
            
            sm=max(sm,(arr[i]+arr[n-1-i]))
        return sm
            
        
        