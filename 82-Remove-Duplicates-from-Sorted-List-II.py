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
        while curr:
            val = curr.val
            temp = curr
            while temp and temp.val == val:
                temp = temp.next
            if curr.next != temp:
                if curr == head and temp and not temp.next:
                    head = temp
                    break
                if curr == head and not temp:
                    head = None
                    break
                if curr != head and not temp:
                    curr2 = head
                    while curr2.next != curr:
                        curr2 = curr2.next
                    curr2.next = None
                    break
                if curr != head and temp:
                    curr2 = head
                    while curr2.next != curr:
                        curr2 = curr2.next
                    curr2.next = temp
                    curr = temp
                    continue
                if curr == head and temp and temp.next:
                    head = temp
                    curr = temp
                    continue
            curr = curr.next
        return head