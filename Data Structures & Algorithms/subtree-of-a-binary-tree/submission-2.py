# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        s1, s2 = [], []

        def preorder(root, acc):
            if not root:
                acc.append('x')
                return
            
            acc.append(f"({root.val})")

            preorder(root.left, acc)
            preorder(root.right, acc)

        preorder(root, s1)
        preorder(subRoot, s2)

        s1 = "".join(s1)
        s2 = "".join(s2)

        return s2 in s1