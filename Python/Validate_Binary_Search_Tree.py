# 98. Validate Binary Search Tree

def isValidBST(self, root: Optional[TreeNode]) -> bool:
    def helper(node, lower_limit, upper_limit):
        if node is None:
            return True
        if node.val <= lower_limit or node.val >= upper_limit:
            return False
        return helper(node.left, lower_limit, node.val) and helper(node.right, node.val, upper_limit)

    return helper(root, float('-inf'), float('inf'))
