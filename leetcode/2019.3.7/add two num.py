class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def addTwoNumbers(l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        l3 = ListNode(0)
        head = l3
        carry = 0
        while l1 and l2:
            l3.next = ListNode(0)
            l3 = l3.next
            l3.val = (l1.val + l2.val + carry) % 10
            carry = (l1.val + l2.val + carry) // 10
            l1 = l1.next
            l2 = l2.next
        while l1:
            l3.next = ListNode(0)
            l3 = l3.next
            l3.val = (l1.val + carry) % 10
            carry = (l1.val + carry) // 10
            l1 = l1.next
        while l2:
            l3.next = ListNode(0)
            l3 = l3.next
            l3.val = (l2.val + carry) % 10
            carry = (l2.val + carry) // 10
            l2 = l2.next
        if carry != 0:
            l3.next = ListNode(0)
            l3 = l3.next
            l3.val = carry
            l3.next = None
        return head.next

if __name__ == "__main__":
    pass