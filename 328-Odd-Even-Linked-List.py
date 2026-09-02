# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        if not head or not head.next or not head.next.next:
            return head
    
        cntr = 1
        prev, curr = None, head
        length = 1
        temp = head
        while temp.next:
            temp = temp.next
            length += 1
        tail = temp
        while cntr != length + 1:
            if cntr % 2 == 0:
                prev.next = curr.next
                tail.next = curr
                curr.next = None
                tail = curr
                curr = prev.next
            else:
                prev = curr
                curr = curr.next
            cntr += 1
        return head