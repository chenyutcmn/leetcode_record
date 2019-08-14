
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        temp = head
        count = 1
        while(temp != None):
            head = head.next
            count += 1
        temp = head
        indx = count- k % count
        count = 1
        while(count != indx):
            temp = temp.next
        new_head = temp.next
        temp.next = None
        while(new_head.next != None):
            new_head = new_head.next
        new_head.next = head


if __name__ == "__main__":
    
        