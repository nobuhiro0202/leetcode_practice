class Solution:
    def arraySign(self, nums: List[int]) -> int:
        r = 1
        for num in nums:
            if num == 0: return 0
            r = r * 1 if num > 0 else r * -1

        return r