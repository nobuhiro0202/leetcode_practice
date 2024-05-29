class Solution(object):
  def twoSum(self, nums, target):
    d = {}
    for i, j in enumerate(nums):
      c = target - j
      if c in d: return [d[c], i]
      d[j] = i
    return None

s = Solution()
a = [3,2,4]
t = 6
r = s.twoSum(a, t)
print(r)