"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return None

        clones = {node: Node(node.val)} 
        q = deque([node])

        while q:
            orig = q.popleft()
            for nb in orig.neighbors:
                if nb not in clones:
                    clones[nb] = Node(nb.val)  
                    q.append(nb)
                clones[orig].neighbors.append(clones[nb])

        return clones[node]