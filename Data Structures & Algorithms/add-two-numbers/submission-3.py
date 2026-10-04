# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# O(max(l1,l2)) time, O(max(l1,l2)) space
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        tail = dummy
        carry = 0
        while l1 or l2 or carry>0:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            total = val1 + val2 + carry
            carry = total // 10
            tail.next = ListNode(total % 10)
            tail = tail.next
            if l1: l1 = l1.next
            if l2: l2 = l2.next
        return dummy.next

# same solution using a built-in function divmod()
# class Solution:
#     def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
#         dummy = ListNode(0)
#         tail = dummy
#         carry = 0
#         while l1 or l2 or carry:
#             val1 = l1.val if l1 else 0
#             val2 = l2.val if l2 else 0          
#             # divmod returns (quotient, remainder) -> (carry, digit_value)
#             # make the code slightly cleaner and faster in Python by utilizing the built-in function divmod(), which computes both the quotient and the remainder in a single operation.
#             carry, out = divmod(val1 + val2 + carry, 10)           
#             tail.next = ListNode(out)
#             tail = tail.next           
#             if l1: l1 = l1.next
#             if l2: l2 = l2.next           
#         return dummy.next
