class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        curr1, curr2 = l1, l2
        carry = 0
        while curr1 and curr2:
            res = curr1.val + curr2.val + carry
            if res > 9:
                carry = 1
                curr1.val = res % 10
                if not curr1.next:
                    curr1.next = ListNode(0)
            else:
                carry = 0
                curr1.val = res
    
            curr1 = curr1.next
            curr2 = curr2.next

        while curr1 and carry:
            res = curr1.val + carry
            if res > 9:
                carry = 1
                curr1.val = res % 10
                if not curr1.next:
                    curr1.next = ListNode(0)
            else:
                carry = 0
                curr1.val = res
            curr1 = curr1.next
        if curr2 and not curr1:
            temp = l1
            while temp.next:
                temp = temp.next
            while curr2:
                temp.next = ListNode(curr2.val)
                temp = temp.next
                curr2 = curr2.next
        return l1
