# 114. Flatten Binary Tree to Linked List

def flatten(self, root: Optional[TreeNode]) -> None:
    """
    Do not return anything, modify root in-place instead.
    """
    if root is None:
        return

    stack = []
    stack.append(root)
    while len(stack) > 0:
        node = stack.pop()
        if node.right is not None:
            stack.append(node.right)
        if node.left is not None:
            stack.append(node.left)
        if len(stack) > 0:
            node.left = None
            node.right = stack[-1]
