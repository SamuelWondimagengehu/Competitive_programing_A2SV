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
    public ListNode insertionSortList(ListNode head) {
        ListNode dummy = new ListNode(0,head);
        ListNode current = head.next;
        ListNode prev = head;

        while(current != null) {
            if(current.val >= prev.val) {
                prev = current;
                current = current.next;
                continue;
            }

        ListNode temp = dummy;
        while(current.val > temp.next.val) {
            temp = temp.next;
        }

        prev.next = current.next;
        current.next = temp.next;
        temp.next = current;
        current = prev.next;
            
        }

        return dummy.next;
    }
}
