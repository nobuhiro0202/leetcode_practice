# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
  def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
    s = head
    f = head
    while f.next is not None:
      s = s.next
      if f.next.next is None: break
      f = f.next.next
    return s