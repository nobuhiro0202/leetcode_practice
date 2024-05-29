# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
  def pairSum(self, head: Optional[ListNode]) -> int:
    slow, fast = head, head
    while fast:
      fast = fast.next.next
      slow = slow.next
      
    p = None
    while slow:
      slow.next, p, slow = p, slow, slow.next

    m = 0
    while p:
      m = max(m, head.val + p.val)
      head = head.next
      p = p.next
    return m