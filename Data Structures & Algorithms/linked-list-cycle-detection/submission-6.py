# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# class Solution:
#     def hasCycle(self, head: Optional[ListNode]) -> bool:
#         seen = {}
#         current = head
#         while current:
#             if current in seen:
#                 return True
#             seen[current] = seen.get(current, 0) + 1
#             current = current.next
#         return False

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        seen = set() # using set(hashset) is cleaner and faster than a dictionary(hashmap)
        current = head
        while current:
            if current in seen:
                return True
            seen.add(current)
            current = current.next
        return False
