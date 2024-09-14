# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def gcd(a, b):
          if a == 0:
            return b

          return gcd(b % a, a)
        
        curr = head

        while curr.next:
          nxt = curr.next
          # find gcd of curr.val and curr.next -> temp
          temp = ListNode(gcd(curr.val, nxt.val), nxt)
          curr.next = temp
          curr = nxt

        return head
    





        
