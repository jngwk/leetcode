# Definition for singly-linked list.
# class ListNode
#     attr_accessor :val, :next
#     def initialize(val = 0, _next = nil)
#         @val = val
#         @next = _next
#     end
# end
# @param {ListNode} head
# @return {ListNode}
def insert_greatest_common_divisors(head)
  cur = head
  while cur.next
    insert = ListNode.new(cur.val.gcd(cur.next.val), cur.next)
    cur.next = insert
    cur = insert.next
  end
  head
end
