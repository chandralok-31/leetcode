/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public boolean isPalindrome(ListNode head) {
        if(head==null || head.next==null){
            return true;
        }
        ListNode slow=head;
        ListNode fast=head;
        while(fast!=null && fast.next!=null){
            slow=slow.next;
            fast=fast.next.next;
          
        }
        ListNode prev=null;
        while (slow!=null){
            ListNode nxt=slow.next;
            slow.next=prev;
            prev=slow;
            slow=nxt;
        }
        ListNode left=head;
        ListNode right=prev;
        while(left!=null && right!=null){
            if(left.val!=right.val){
                return false;
            }
            left=left.next;
            right=right.next;
        }
        return true;
        
    }
}

// fast,slow=head,head
//         while fast and fast.next:
//             fast=fast.next.next
//             slow=slow.next
//         prev=None
//         while slow:
//             nxt=slow.next
//             slow.next=prev
//             prev=slow
//             slow=nxt
//         left,right=head,prev
//         while right:
//             if left.val!=right.val:
//                 return False
//             left=left.next
//             right=right.next
//         return True