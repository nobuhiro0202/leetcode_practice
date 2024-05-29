# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
  def swapPairs(self, head: ListNode) -> ListNode:
    """
    :type head: ListNode
    :rtype: ListNode
    """

    # If the list has no node or has only one node left.
    if not head or not head.next: return head

    # Nodes to be swapped
    f = head
    s = head.next

    # Swapping
    f.next = self.swapPairs(s.next)
    s.next = f

    # Now the head is the second node
    return s