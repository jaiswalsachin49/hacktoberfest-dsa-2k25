# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head == None or k == 0:
            return head
        
        l = 1
        i = head
        while i.next:
            l += 1
            i = i.next
        k = k % l
        if k == 0:
            return head
        
        i.next = head
        j = l - k
        m = i
        while j:
            m = m.next
            j -= 1
        head = m.next
        m.next = None
        return head
