from collections import Counter
class Solution:
  def commonChars(self, words: List[str]) -> List[str]:
    d = {}
    for c in words[0]: d[c] = d.get(c, 0) + 1
    for word in words[1:]:
        word_counter = Counter(word)
        for char in d: d[char] = min(d[char], word_counter[char])

    result = []
    for char, count in d.items(): result.extend([char] * count)
    return result
  