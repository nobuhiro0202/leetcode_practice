class Solution:
  def simplifyPath(self, path: str) -> str:
    parts = path.split('/')
    stack = []
    for part in parts:
      if part == '.' or not part: continue
      elif part == '..':
        if stack: stack.pop()
      else: stack.append(part)
    return '/' + '/'.join(stack)