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



# ########### 237

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val=node.next.val
        node.next=node.next.next


##################### 680
class Solution:
    def validPalindrome(self, s: str) -> bool:
        l=0
        r=len(s)-1
        while l<r:
            if s[l]!=s[r]:
                skipL,skipR=s[l+1:r+1],s[l:r]
                return (skipL==skipL[::-1]) or (skipR==skipR[::-1])
            l=l+1
            r=r-1
        return True



############### 328
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head==None or head.next==None :
            return head
        odd,even=head,head.next
        Even=even
        while odd.next and even.next:
            odd.next=odd.next.next
            even.next=even.next.next
            
            odd=odd.next
            even=even.next
        odd.next=Even
        return head


############# 445
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        word1=""
        word2=""
        while l1:
            word1+=str(l1.val)
            l1=l1.next
        while l2:
            word2+=str(l2.val)
            l2=l2.next 
        num=str(int(word1)+int(word2))
        n=len(num)
        head=ListNode(int(num[0]))
        ptr=head
        for i in range(1,n):
            head.next=ListNode(int(num[i]))
            head=head.next
        return ptr



############### 771
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        count=0
        for i in jewels:
            count=count+stones.count(i)
        return count