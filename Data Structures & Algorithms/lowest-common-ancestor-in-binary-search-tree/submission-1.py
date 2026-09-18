# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        current = root

        while current:
            if p.val < current.val and q.val < current.val: # If both p and q are smaller than current node, move to the left subtree
                current = current.left
            elif p.val > current.val and q.val > current.val: # If both p and q are greater than current node, move to the right subtree
                current = current.right
            else:  # We found the split point or one of the nodes matches current
                return current