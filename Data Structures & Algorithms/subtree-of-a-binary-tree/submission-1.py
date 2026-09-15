# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Time Complexity: \(O(M \times N)\) where M is the number of nodes in root and N is the number of nodes in subRoot. In the worst-case scenario, isSameTree is called for every node in the main tree.
# Space Complexity: \(O(H_{root})\) where \(H_{root}\) is the height of the main tree, due to the recursion stack frames.
class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root is None:
            return False
        if self.isChildSub(root, subRoot):
            return True
        a1 = self.isSubtree(root.left, subRoot)
        a2 = self.isSubtree(root.right, subRoot)
        return a1 or a2
    def isChildSub(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root is None and subRoot is None:
            return True
        if root is None or subRoot is None:
            return False
        if subRoot.val == root.val:
            a1 = self.isChildSub(root.left, subRoot.left)
            a2 = self.isChildSub(root.right, subRoot.right)
            return a1 and a2