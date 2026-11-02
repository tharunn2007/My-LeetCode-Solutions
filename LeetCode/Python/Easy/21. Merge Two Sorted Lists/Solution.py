# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
        
        dummy_node = ListNode(0)
        current = dummy_node
        #since we move across the new list we create dummy node and point it to next one


        while list1 and list2 : 
            if list1.val<=list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
        #normal comparision and traversing 
        
        if list1: #if list2 is null then whe rest of list1 present then we directly add 
            current.next = list1
        else: #complementary of the if statement
            current.next = list2
        return dummy_node.next