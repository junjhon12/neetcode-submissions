class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self):
        # The LinkedList tracks a dummy head and the total size
        self.dummy = Node(0)
        self.size = 0
    
    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1

        curr = self.dummy.next
        for _ in range(index):
            curr = curr.next
        return curr.val

    def insertHead(self, val: int) -> None:
        new_node = Node(val)
        new_node.next = self.dummy.next
        self.dummy.next = new_node
        self.size += 1

    def insertTail(self, val: int) -> None:
        curr = self.dummy
        while curr.next:
            curr = curr.next
        curr.next = Node(val)
        self.size += 1

    def remove(self, index: int) -> bool:
        if index < 0 or index >= self.size:
            return False
        
        curr = self.dummy
        for _ in range(index):
            curr = curr.next
        
        # Fixed typo: changed '=' to '.' to bypass the deleted node
        curr.next = curr.next.next 
        self.size -= 1
        return True

    def getValues(self) -> list[int]:
        res = []
        curr = self.dummy.next
        while curr:
            res.append(curr.val)
            curr = curr.next
        return res