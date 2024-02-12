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
    public ListNode removeNthFromEnd(ListNode head, int n) {
        ListNode dummy = head;
        int nodes = 0;
        
        while(dummy != null) {
            nodes++;
            dummy = dummy.next;
        }
        nodes = nodes - n;
        ListNode prev = null;
        ListNode curr = head;
        
        if(nodes == 0 || nodes == -1) {
            return head.next;
        }
        
        while(nodes > 0) {
            prev = curr;
            curr = curr.next;
            nodes--;
        }
        prev.next = curr.next;
        
        return head;
    }
}