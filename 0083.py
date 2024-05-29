class Solution:
  def deleteDuplicates(self, head: ListNode) -> ListNode:
    c = head
    while c is not None and c.next is not None:
      if c.next.val == c.val: c.next = c.next.next
      else: c = c.next
    return head