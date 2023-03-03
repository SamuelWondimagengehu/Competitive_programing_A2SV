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
        if(head.next == null) return true;
        if(head == null) return false;

        ListNode fast = head;
        ListNode slow = head;
        ListNode h1 = head;
        ListNode prev = null;

        while(fast != null && fast.next != null) {
            fast = fast.next.next;
            prev = slow;
            slow = slow.next;
        }

        prev.next = null;
        ListNode l1 = reverse(slow);

        while(h1 != null) {
            if(h1.val == l1.val) {
                h1 = h1.next;
                l1 = l1.next;
            } else return false;
        }
        return true;
    }

    public ListNode reverse(ListNode l1) {
        ListNode current_node = l1;
        ListNode prev = null;

        while(current_node != null) {
            ListNode next = current_node.next;
            current_node.next = prev;
            prev = current_node;
            current_node = next;
        }

        return prev;
    }
}
