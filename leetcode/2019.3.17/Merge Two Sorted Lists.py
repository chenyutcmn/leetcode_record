# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if  l1 != None and l2 != None:
            if l1.val < l2.val:
                l1.next =  self.mergeTwoLists(l1.next , l2)
                return l1
            else:
                l2.next = self.mergeTwoLists(l1 , l2.next)
                return l2
        elif l1 == None:
            return l2
        elif l2 == None: 
            return l1
        
        