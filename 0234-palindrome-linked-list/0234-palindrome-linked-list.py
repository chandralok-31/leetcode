# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        str1=""
        temp=head
        while temp:
            str1+=str(temp.val)
            temp=temp.next
        return str1==str1[::-1]
        