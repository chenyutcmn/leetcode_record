# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if head == None:
            return None
        elif head.next == None:
            return head
        else:
            temp = head.next
            if temp.next != None:
                head.next = self.swapPairs(temp.next)
            else:
                head.next = None
            temp.next = head
            return temp 