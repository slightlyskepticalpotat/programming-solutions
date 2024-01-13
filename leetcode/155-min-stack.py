class MinStack:

    def __init__(self):
        self.vals, self.mins = [], [float("inf")]

    def push(self, val: int) -> None:
        self.vals.append(val)
        if val <= self.mins[-1]:
            self.mins.append(val)

    def pop(self) -> None:
        if self.mins[-1] == self.vals.pop():
            self.mins.pop()

    def top(self) -> int:
        return self.vals[-1]

    def getMin(self) -> int:
        return self.mins[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()