import bisect
class Solution:
  def lastStoneWeight(self, stones: List[int]) -> int:
    stones.sort()
    def smash(x, y):
      if x == y: return None
      if x != y: return y - x
    while len(stones) > 1:
      y = stones.pop()
      x = stones.pop()
      s = smash(x, y)
      if s: stones.insert(bisect.bisect_left(stones, s), s)
      if len(stones) == 0: return 0
    return stones[0]
      