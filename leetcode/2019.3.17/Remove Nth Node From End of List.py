#边界条件 边界条件！

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        i = head
        j = head
        for k in range(n):
            j = j.next
        if j == None:
            return head.next
        while j.next != None:
            j = j.next
            i = i.next
        i.next = (i.next).next
        return head
        
        