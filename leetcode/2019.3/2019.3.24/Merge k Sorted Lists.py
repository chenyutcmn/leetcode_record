#分治法的应用
#想清楚再下笔

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if len(lists) <= 2:
            return self.mergeTwoList(lists)
        mid = len(lists) // 2
        left = self.mergeKLists(lists[0:mid])
        right = self.mergeKLists(lists[mid:len(lists)])
        newlists = [left , right]
        return self.mergeTwoList(newlists)
    def mergeTwoList(self , lists):
        if lists == []:
            return None
        elif len(lists) == 1:
            return lists[0]
        else:
            if lists[0] == None:
                return lists[1]
            elif lists[1] == None:
                return lists[0]
            elif lists[0].val < lists[1].val:
                lists[0].next = self.mergeTwoList([lists[0].next , lists[1]])
                return lists[0]
            else:
                lists[1].next = self.mergeTwoList([lists[0] , lists[1].next])
                return lists[1]
                
                