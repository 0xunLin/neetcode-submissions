# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        curr = root
        
        while stack or curr:
            # 1. Travel as far left as possible
            while curr:
                stack.append(curr)
                curr = curr.left
            
            # 2. Process the current node
            curr = stack.pop()
            k -= 1
            if k == 0:
                return curr.val
            
            # 3. Move to the right subtree
            curr = curr.right
