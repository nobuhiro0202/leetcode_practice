class Solution:
  def maxProfit(self, prices: List[int]) -> int:
    m = float("inf")
    p = 0
    for i in range(len(prices)):
      if prices[i] < m: m = prices[i]
      elif prices[i] - m > p: p = prices[i] - m

    return p