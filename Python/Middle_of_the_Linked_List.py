# 876. Middle of the Linked List

def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
    slow = head
    fast = head
    while slow and fast is not None:
        if fast.next is None:
            return slow
        slow = slow.next
        fast = fast.next.next
    return slow

# better solution:


def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow
