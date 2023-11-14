# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        bina = ''
        while head.next is not None:
            bina += str(head.val)
            head = head.next
        bina += str(head.val)
        return int(bina,2)