# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        stack = []
        current = root
        previous_value = float('-inf')

        while stack or current:
            #lets go left
            while current:
                stack.append(current)
                current = current.left
            current = stack.pop()
            if current.val <= previous_value:
                return False
            previous_value = current.val
            current = current.right
        return True