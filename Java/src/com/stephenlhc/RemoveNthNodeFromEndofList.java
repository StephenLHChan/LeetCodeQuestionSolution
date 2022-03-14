package com.stephenlhc;

public class RemoveNthNodeFromEndofList {
//  19. Remove Nth Node From End of List

    public ListNode removeNthFromEnd(ListNode head, int n) {
        var slow = head;
        var fast = head;

        for(int i = 0; i < n; i++)
            fast = fast.next;

        if(fast == null){
            head = head.next;
            return head;
        }

        while(fast.next != null){
            slow = slow.next;
            fast = fast.next;
        }

        slow.next = slow.next.next;

        return head;
    }
}
