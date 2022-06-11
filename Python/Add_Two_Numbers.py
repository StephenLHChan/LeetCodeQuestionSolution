# 2. Add Two Numbers

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    carryForward = 0
    root = ListNode(0)
    n = root
    while carryForward or l1 or l2:
        l1_val = 0
        l2_val = 0
        if l1:
            l1_val = l1.val
            l1 = l1.next
        if l2:
            l2_val = l2.val
            l2 = l2.next
        carryForward = carryForward + l1_val + l2_val
        n.next = ListNode(carryForward % 10)
        n = n.next
        carryForward //= 10
    return root.next
