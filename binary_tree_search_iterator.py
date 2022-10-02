# memory: O(h), time: O(1) avg
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val=val
        self.left = left
        self.right = right

class BSTIterator:
    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        cur = root
        while cur:
            self.stack.append(cur)
            cur = cur.left

    def next(self):
        result = self.stack.pop()
        cur = result.right
        #add all left nodes of right node if it exists
        while cur:
            self.stack.append(cur)
            cur = cur.left
        return res.val

    def hasNext(self) -> bool:
        return self.stack == []
