# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the root node in the tree
    def __init__(self):
        self.cur = None

    def size(self):
        head = self.cur
        count = 0
        while head is not None:
            head = head.next
            count += 1
        return count

    def generate(self, n):
        if n <= 0:
            return None
        left = self.generate(n / 2)
        root = self.cur
        self.cur = self.cur.next
        root.left = left
        right = self.generate(n - n / 2 - 1)
        root.right = right
        return root

    def sortedListToBST(self, A):
        if A is None:
            return None
        self.cur = A

        n = self.size()
        root = self.generate(n)
        return root
