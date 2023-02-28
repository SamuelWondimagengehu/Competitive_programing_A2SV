static boolean hasCycle(SinglyLinkedListNode head) {
        SinglyLinkedListNode fast = head.next;
        SinglyLinkedListNode slow = head;
        
        while(fast != null && fast.next != null) {
            if(fast == slow) return true;
            fast = fast.next.next;
            slow = slow.next;
        }
        return false;
    }
