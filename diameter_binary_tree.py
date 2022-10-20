class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val=val
        self.left = left
        self.right = right

def diameter_tree(root: TreeNode) -> int:
    result = [0]

    def dfs(root):
        if not root:
            return -1   # height when node is null

        left = dfs(root.left)
        right = dfs(root.right)
        result[0] = max(result[0], 2+left+right) # new max diameter

        return 1 + max (left, right) # new max height

    dfs(root)
    return result[0]
