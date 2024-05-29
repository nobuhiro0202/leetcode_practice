class Solution:
  def diagonalSum(self, mat: List[List[int]]) -> int:
    ans = 0
    s = len(mat)
    for i in range(s):
      if i == s - i - 1:
        ans += mat[i][i]
        continue
      ans += mat[i][i]
      ans += mat[i][s-i-1]
    return ans

a = Solution()
mat = [[1,2,3], [4,5,6], [7,8,9]]
a.diagonalSum(mat)