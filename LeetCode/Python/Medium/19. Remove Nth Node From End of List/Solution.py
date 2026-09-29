# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        if head==None:
            return head
        elif head.next==None:
            head = None
            return head
        else:
            c=head
            k=None
            count=0
            u=head
            
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
            