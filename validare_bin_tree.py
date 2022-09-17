class TreeNode():
    def __init__(self, val=0, left=None, right=None):
        self.val=val
        self.left = left
        self.right = right


# O(n) * O(n) - check left and right and update boundaries
# root has -inf < root < inf boundary
# lefts: -inf < lval < root
# rights: root <rval < inf

def isvalidBST(self, root: TreeNode) -> bool:
    def validNode(node, leftBound, rightBound): # helper function
        if not node:
            return True

        if not (node.val < rightBound and node.val > leftBound):
            return False

        return (validNode(node.left, leftBound, node.val) and
                validNode(node.right, node.val, rightBound) )

    return validNode(root, float("-inf"), float("inf"))



