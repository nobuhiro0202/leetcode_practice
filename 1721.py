class Solution:
  def swapNodes(self, head: ListNode, k: int) -> ListNode:
    l = 0
    f, e, c = None, None, head
    
    while c:
      l += 1
      if e is not None: e = e.next
      if l == k:
        f = c
        e = head
      c = c.next
  
    f.val, e.val = e.val, f.val
    return head