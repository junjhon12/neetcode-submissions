class LinkedList:
    
    def __init__(self):
        self.arr = []
    
    def get(self, index: int) -> int:
        if index + 1 > len(self.arr):
            return -1
        return self.arr[index]

    def insertHead(self, val: int) -> None:
        self.arr.insert(0, val)

    def insertTail(self, val: int) -> None:
        self.arr.append(val)

    def remove(self, index: int) -> bool:
        if index + 1 > len(self.arr):
            return False
        self.arr.pop(index)
        return True

    def getValues(self) -> List[int]:
        return self.arr
