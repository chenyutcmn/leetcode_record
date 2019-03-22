#9次提交才做对，lzzscl ffffffffff**k

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return head
        temp = head
        headtemp = None
        headtag = 0
        mydeque = collections.deque()
        i = 0
        while head:
            mydeque.append(head)
            head = head.next
            i += 1
            if i == k:
                while mydeque:
                    if headtag == 0:
                        headtemp = mydeque.pop()
                        temp = headtemp
                        headtag = 1
                    else:
                        temp.next = mydeque.pop()
                        temp = temp.next 
                i = 0
        if i != 0:
            while mydeque:
                if headtag == 0:
                    headtemp = mydeque.popleft()
                    temp = headtemp
                    headtag = 1
                else:
                    temp.next = mydeque.popleft()
                    temp = temp.next
        temp.next = None
        return headtemp
