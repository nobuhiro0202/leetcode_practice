from bisect import bisect_left
class Solution:
  def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
    nums.sort()
    n = len(nums)
    s = [0] * (n + 1)
    for i in range(n): s[i + 1] = s[i] + nums[i]
    ans = []
    for q in queries:
      p = bisect_left(s, q)
      if (p == n + 1) or (s[p] > q): p -= 1
      ans.append(p)
    return ans