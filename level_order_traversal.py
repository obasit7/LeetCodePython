import collections


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val=val
        self.left = left
        self.right = right

def level_order_traversal(root: TreeNode):
    result = []
    q = collections.deque()
    q.append(root)

    while q:
        queue_length = len(q)
        level_nodes = []
        # to iterate over only the same level
        for i in range(queue_length):
            node = q.popleft()
            if node:
                # if node exists, add it to the level and its children to queue
                level_nodes.append(node.val)
                q.append(node.left)
                q.append(node.right)

        if level_nodes:
            result.append(level_nodes)

    return result



