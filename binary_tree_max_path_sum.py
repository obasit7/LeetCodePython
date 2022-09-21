# Hard

class TreeNode():
    def __init__(self, val=0, left=None, right=None):
        self.val=val
        self.left = left
        self.right = right

def max_path(root: TreeNode):
    res = [root.val]

    #returns max path sum without splitting
    def dfs(root):
        if not root: #if root is null
            return 0

        leftMax = dfs(root.left)
        rightMax = dfs(root.right)

        leftMax = max(leftMax, 0)
        rightMax = max(rightMax, 0)

        # computing max path WITH split
        res[0] = max(res[0], root.val + leftMax +rightMax)

        return root.val + max(leftMax, rightMax)

    dfs(root)
    return res[0]




