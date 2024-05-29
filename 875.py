import math
class Solution:
  def minEatingSpeed(self, piles: List[int], h: int) -> int:
    l, r = 1, max(piles)
    while l < r:
      a = 0
      m = (l + r) // 2
      for i in piles: a += math.ceil(i / m)
      if a <= h: r = m
      else: l = m + 1
    return l