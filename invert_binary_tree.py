class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val=val
        self.left = left
        self.right = right


root = TreeNode(3)
node1 = TreeNode(2)
node2 = TreeNode(4)

root.left = node1
root.right = node2

def invert_tree(root: TreeNode) -> TreeNode:
    if not root:
        return
    temp = root.right
    root.right = root.left
    root.left = temp

    invert_tree(root.left)
    invert_tree(root.right)

    return root

def print_inorder(root: TreeNode):
    arr_nodes = []
    def inorder(root):
        if not root:
            return
        inorder(root.left)
        arr_nodes.append(root.val)
        inorder(root.right)
    inorder(root)
    print(arr_nodes)


print_inorder(root)
invert_tree(root)
print_inorder(root)
