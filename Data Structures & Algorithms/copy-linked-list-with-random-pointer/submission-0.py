"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        temp = head
        while temp:
            node = Node(temp.val)
            node.next = temp.next
            temp.next = node
            temp = node.next

        temp = head
        while temp:
            node = temp.next 
            if temp.random:
                node.random = temp.random.next
            temp = node.next 
            
        newHead = head.next
        temp = head
        while temp:
            node = temp.next
            temp.next = node.next 
            
            if node.next:
                node.next = node.next.next
            
            temp = temp.next
            
        return newHead