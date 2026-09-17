class MinStack:

    def __init__(self):
        self.st = []
        self.minSt = []
    def push(self, val: int) -> None:
        self.st.append(val)
        if not self.minSt or val <= self.minSt[-1]:
            self.minSt.append(val)
        else:
            self.minSt.append(self.minSt[-1])
    def pop(self) -> None:
        if not self.st:
            return 
        self.st.pop()
        self.minSt.pop()


    def top(self) -> int:
        if not self.st:
            return -1
        return self.st[-1]

    def getMin(self) -> int:
        if not self.minSt:
            return -1
        return self.minSt[-1]
