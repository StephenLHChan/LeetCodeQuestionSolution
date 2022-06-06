# 160. Intersection of Two Linked Lists

def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
    seen = set()

    curr = headA
    while curr:
        seen.add(curr)
        curr = curr.next

    curr = headB
    while curr:
        if curr in seen:
            return curr
        curr = curr.next
    return None
