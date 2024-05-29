import re
class Solution:
  def isPalindrome(self, s: str) -> bool:
    s = re.sub(r"[^a-zA-Z0-9]", "", s).lower()
    return s == s[::-1]
    
s = Solution()
a = s.isPalindrome('0P')
print(a)
