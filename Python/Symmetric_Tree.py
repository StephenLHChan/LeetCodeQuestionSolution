# 101. Symmetric Tree

def isSymmetric(self, root: Optional[TreeNode]) -> bool:

    def isSym(leftTree, rightTree):
        if not leftTree and not rightTree:
            return True
        if leftTree and rightTree and leftTree.val == rightTree.val:
            return isSym(leftTree.left, rightTree.right) and isSym(leftTree.right, rightTree.left)
        else:
            return False

    return isSym(root.left, root.right)
