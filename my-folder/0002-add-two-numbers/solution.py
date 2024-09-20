# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def getNumber(node):
            curr = node
            place = 1
            num = 0
            while curr:
                num += curr.val * place
                curr = curr.next
                place *= 10
            return num

        result = getNumber(l1) + getNumber(l2)

        dummy = ListNode()
        current = dummy
        
        if result == 0:
            return ListNode(0)
        
        while result > 0:
            digit = result % 10
            result //= 10
            current.next = ListNode(digit)
            current = current.next

        return dummy.next
