class Solution {
    public ListNode middleNode(ListNode head) {
        ListNode current = head;
        int size = 0;
        
        while(current != null) {
            current = current.next;
            size++;
        }        
        size /= 2;
        current = head;

        while(size > 0) {
            current = current.next;
            size--;
        }

        return current;
    }
}
