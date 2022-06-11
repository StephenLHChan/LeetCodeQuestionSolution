# 19. Remove Nth Node From End of List

def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
    fast = head
    slow = head
    for _ in range(n):
        fast = fast.next

    if not fast:
        return head.next

    while fast.next:
        fast = fast.next
        slow = slow.next
    slow.next = slow.next.next
    return head
