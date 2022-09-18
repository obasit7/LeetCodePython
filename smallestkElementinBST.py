# given root of BST, return kth smallest element in BST

class TreeNode():
    def __init__(self, val=0, left=None, right=None):
        self.val=val
        self.left = left
        self.right = right

# convert BST into an array, take kth element
#        3
#     1      4        ---inorder traversal ---> [0,1,2,3,4,5]
#    0  2      5

#use stack for iterative push current root, visit left, push
def kthSmallest(root: TreeNode, k:int) -> int:
    n = 0 # number of elements visited. When n=k, return that value
    stack = []
    curr = root

    while curr or stack:
        while curr:
            stack.append(curr) # [3, 1]
            curr = curr.left
        curr = stack.pop()
        n += 1
        if n == k:
            return curr.val
        curr = curr.right




