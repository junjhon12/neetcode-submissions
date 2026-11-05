"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        copyMap = {}
        copyMap[node] = Node(node.val)
        q = deque([node])
        while q:
            curr = q.popleft()
            for n in curr.neighbors:
                if n not in copyMap:
                    copyMap[n] = Node(n.val)
                    q.append(n)
                copyMap[curr].neighbors.append(copyMap[n])
        return copyMap[node]
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return None

        clones = {node: Node(node.val)}     # register start before the loop
        q = deque([node])

        while q:
            orig = q.popleft()
            for nb in orig.neighbors:
                if nb not in clones:
                    clones[nb] = Node(nb.val)   # register BEFORE enqueue
                    q.append(nb)
                clones[orig].neighbors.append(clones[nb])

        return clones[node]