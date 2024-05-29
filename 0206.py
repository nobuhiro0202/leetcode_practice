class Solution:
  def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    curr = head
    prev = None
    while curr is not None:
      n = curr.next
      curr.next = prev
      prev = curr
      curr = n
    return prev