# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        n = head
        l = 0
        while n:
            l += 1
            n = n.next   
        start = l//2
        n = head
        i = 0
        while i < start:
            n = n.next
            i += 1
        new = ListNode(n.val) 
        head = new
        while n.next:
            n = n.next
            new.next = ListNode(n.val)  # Create a new node for each subsequent node
            new = new.next
        return head