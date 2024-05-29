class Solution:
  def reorderList(self, head: ListNode) -> None:
    slow = fast = head
    while fast and fast.next:
      slow = slow.next
      fast = fast.next.next

    prev, curr = None, slow
    while curr:
      n = curr.next
      curr.next = prev
      prev = curr
      curr = n

    first, second = head, prev
    while second.next:
      first.next, first = second, first.next
      second.next, second = first, second.next
    return head