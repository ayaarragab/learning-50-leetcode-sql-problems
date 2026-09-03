# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head or not head.next:
            return head
    
        curr = head

        while curr and curr.next:
            val = curr.val
            temp = curr.next
            while temp and temp.val == val:
                save = curr.next
                curr.next = curr.next.next
                save.next = None
                temp = curr.next
            curr = temp
        return head