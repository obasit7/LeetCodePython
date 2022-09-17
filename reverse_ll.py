# recursively or pointers
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# T: O(n)
def reverse(self, head: ListNode) -> ListNode:
    prev, curr = None, head
    while curr:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp
    return prev

