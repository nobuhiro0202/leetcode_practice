class Solution:
  def deleteDuplicates(self, head: ListNode) -> ListNode:
    l = ListNode(0, head)
    r = l
    while head:
      if head.next and head.val == head.next.val:
        while head.next and head.val == head.next.val: head = head.next
        r.next = head.next
      else: r = r.next
      head = head.next

    return l.next