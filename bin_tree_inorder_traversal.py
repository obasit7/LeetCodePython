from typing import List

class TreeNode():
    def __init__(self, val=0, left=None, right=None):
        self.val=val
        self.left = left
        self.right = right

def traverse_inorder(root: TreeNode):
    result = []


    stack = []
    curr = root
    #iterative solution
    while curr or stack:
        while curr:
            stack.append(curr)
            curr = curr.left
        curr = stack.pop()
        result.append(curr.val)
        curr = curr.right
    return result


    #recursive solution
    def inorder(node):
        if not node:
            return
        inorder(node.left)
        result.append(node.val)
        inorder(node.right)

    inorder(root)
    return result




