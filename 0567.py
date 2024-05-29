class Solution:
  def checkInclusion(self, s1: str, s2: str) -> bool:
    if len(s1) > len(s2): return False
    s1map = [0] * 26
    for char in s1: s1map[ord(char) - ord('a')] += 1
    for i in range(len(s2) - len(s1) + 1):
      s2map = [0] * 26
      for j in range(len(s1)): s2map[ord(s2[i + j]) - ord('a')] += 1
      if self.matches(s1map, s2map): return True
    return False
  
  def matches(self, s1map, s2map):
    for i in range(26):
      if s1map[i] != s2map[i]: return False
    return True