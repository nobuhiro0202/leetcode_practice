class Solution:
  def isValid(self, s: str) -> bool:
    d = { '(': ')', '{': '}', '[': ']' }
    a = []
    for c in s:
      if c in d: a.append(c)
      elif len(a) == 0 or c != d[a.pop()]: return False
    return len(a) == 0