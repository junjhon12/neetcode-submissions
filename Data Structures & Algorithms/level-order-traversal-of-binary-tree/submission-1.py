# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
            
        result=[]
        current=[root]

        while current:
            level_val=[]
            next_l=[]

            for i in current:
                level_val.append(i.val)

                if i.left:
                    next_l.append(i.left)

                if i.right:
                    next_l.append(i.right)

            result.append(level_val)
            current=next_l


        return result