# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         val = val
#         next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head or not head.next:
            return head
        prev, curr = None, head
        while curr:
            val = curr.val
            temp = curr
            while temp and temp.val == val:
                temp = temp.next
            if curr.next != temp:
                if curr == head:
                    head = temp
                    curr = temp
                    prev = None
                    continue     
                else:
                    prev.next = temp   
                    curr = temp
                    continue
            prev = curr
            curr = curr.next
        return head