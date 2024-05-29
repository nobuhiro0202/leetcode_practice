class Solution:
  def twoSum(self, numbers: List[int], target: int) -> List[int]:
    d = {}
    r = []
    for i, n in enumerate(numbers): d[target - n] = i
    for i in range(len(numbers)):
      if numbers[i] in d.keys():
        r.append(i + 1)
        r.append(d[numbers[i]] + 1)
        break
    return r