class MinStack:
  def __init__(self):
    self.stack = []
    self.minstk = []

  def push(self, val: int) -> None:
    self.stack.append(val)
    self.minstk.append(min(val, self.minstk[-1] if self.minstk else val))

  def pop(self) -> None:
    self.stack.pop()
    self.minstk.pop()

  def top(self) -> int:
    return self.stack[-1]

  def getMin(self) -> int:
    return self.minstk[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
