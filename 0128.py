class Solution:
  def longestConsecutive(self, nums: List[int]) -> int:
    a = sorted(list(set(nums)))
    m = 0
    p = 0
    for i in range(len(a)):
      p += 1
      if i == len(a) - 1 or a[i] + 1 != a[i + 1]:
        m = max(m, p)
        p = 0
    return m