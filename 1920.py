class Solution:
  def buildArray(self, nums: List[int]) -> List[int]:
    ans = []
    for n in nums: ans.append(nums[n])
    return ans

a = Solution()
arr = [0,2,1,5,3,4]
print(a.buildArray(arr))