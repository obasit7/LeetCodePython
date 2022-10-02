# given inorder and preorder, construct binary tree
# Difficulty: Medium
from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val=val
        self.left = left
        self.right = right

# first val of preorder is root
# first val of inorder is left most
# vals lef to first val of preorder in inorder is on left

# take val of preorder, check place in inorder
# get length of left and right subarrays

# pre: [3, 9, 20, 15, 7], in: [9, 3, 15, 20, 7]
#ans: [3, 9. 20, null, null, 15, 7]

def construct_tree(self, preorder: List[int], inorder: List[int]):
    if not preorder or not inorder:
        return None

    #first val of preorder
    root = TreeNode(preorder[0])
    root_pos = inorder.index(preorder[0]) # 3

    root.left = self.construct_tree(preorder[1:root_pos+1], inorder[:root_pos])
    root.right = self.construct_tree(preorder[root_pos+1:], inorder[root_pos+1:])

    return root


