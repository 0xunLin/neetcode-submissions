# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# O(n) time, O(h) space
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0
        def validate(node: TreeNode, max_so_far):
            nonlocal count
            if not node:
                return
            if node.val >= max_so_far:
                count += 1
                max_so_far = node.val
            validate(node.left, max_so_far)
            validate(node.right, max_so_far)
        validate(root, root.val)
        return count