#9次提交才做对，lzzscl ffffffffff**k
#节点入栈后指针马上移动。注意处理链表尾节点的next域

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        #空链表返回空
        if not head:
            return head
        temp = head         #浮动指针
        headtemp = None     #头节点暂存
        headtag = 0         #头节点标记
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
        #尾节点指向空
        temp.next = None
        return headtemp
