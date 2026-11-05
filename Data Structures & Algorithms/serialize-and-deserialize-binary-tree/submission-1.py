# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        self.res = ''

        def dfs(root):
            if not root:
                self.res += 'n,'
                return

            self.res += str(root.val) + ','
            
            dfs(root.left)
            dfs(root.right)

        return self.res[:-1]
            
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        nodes = data.split(',')
        nodes = [None if i == 'n' else i for i in nodes]

        print(nodes)

        return root