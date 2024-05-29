import math
class Solution:
  def numIdenticalPairs(self, nums: list[int]) -> int:
    # d = {}
    # a = 0
    # for i in range(len(nums)):
    #   if nums[i] in d.keys(): d[nums[i]].append(i)
    #   else: d[nums[i]] = [i]
    # for item in d.values():
    #   if len(item) < 2: continue
    #   a += math.comb(len(item), 2)
    # return a
    s=dict()
    for i in nums:
        if i not in s: s[i]=nums.count(i)
    count=0
    for i in s.values():
        if i>1: count+=sum(range(1,i))
    return count

a = Solution()
nums = [1,2,3,1,1,3]
print(a.numIdenticalPairs(nums))