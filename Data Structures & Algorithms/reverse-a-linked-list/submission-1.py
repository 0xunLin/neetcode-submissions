# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None # to reverse the pointing of the linked lists
        current = head # the first/opening element of the list
        while current: # checking until current is None and the list has been covered, loop runs until there are nodes left to process
            next_node = current.next # storing the remaining part of the linked list after the current head
            current.next = prev # reversing the point to elements
            prev = current # moving the prev reference(pointer) forward, so the next head had point to it
            current = next_node # moving the current reference(pointer) forward to include the next head of the list
        return prev