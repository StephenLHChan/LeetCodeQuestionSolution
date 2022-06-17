# 1290. Convert Binary Number in a Linked List to Integer

def getDecimalValue(self, head: ListNode) -> int:
    res = 0
    current = head
    while current:
        res = res * 2 + current.val
        current = current.next
    return res
