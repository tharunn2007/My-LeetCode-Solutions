# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        #if empty list
        if head==None:
            return head
        #if 1 len list
        elif head.next==None:
            head = None
            return head

        #all other cases
        else:
            c=head
            k=None
            count=0
            u=head
            #edge case where [1,2] having 2 as n
            while u.next:
                count+=1
                u = u.next

            if count - n < 0:
                return head.next

            for i in range(count-n):
                c = c.next
            k = c.next.next
            c.next = k
            return head
            