class Solution:
  def smallerNumbersThanCurrent(self, nums: list[int]) -> list[int]:
    res = []
    hm = {}
    s = sorted(nums)
    for i in range(len(s)):
      if s[i] not in hm: hm[s[i]] = i
    for n in nums: res.append(hm[n])
    return res
