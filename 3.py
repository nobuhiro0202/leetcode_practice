class Solution:
  def lengthOfLongestSubstring(self, s: str) -> int:
    L = ans = 0
    x = set()
    for R in range(len(s)):
      while s[R] in x:
        x.remove(s[L])
        L += 1
      ans = max(R - L + 1, ans)
      x.add(s[R])
    return ans