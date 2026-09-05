# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0) # creating a dummy start to our new linked list
        tail = dummy # the pointer(reference) of the merged list, to the new node to be inserted
        while list1 and list2: # looped and checked as long as both list and list2 have elements to process in them
            
            # for the list with the lower current head value, the merged list tail points to it and the list is pointed to the next element in it, and thus the remaining list
            if list1.val <= list2.val: 
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next

            tail = tail.next # the merged list grows by an element either way, so the tail acts as the newly added node

        # if any of the lists is not empty yet, the merged list tail points(references) to the head of the remaining sorted list elements
        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2
        return dummy.next # return the merged list except the dummy head