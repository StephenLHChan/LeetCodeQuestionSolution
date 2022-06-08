# 1214. Two Sum BSTs

def twoSumBSTs(self, root1: Optional[TreeNode], root2: Optional[TreeNode], target: int) -> bool:
    def getRootValueList(root, ValueList):
        if root:
            ValueList.append(root.val)
            getRootValueList(root.left, ValueList)
            getRootValueList(root.right, ValueList)

    root1ValueList = []
    root2ValueList = []

    getRootValueList(root1, root1ValueList)
    getRootValueList(root2, root2ValueList)

    for item in root1ValueList:
        if (target - item) in root2ValueList:
            return True

    return False
