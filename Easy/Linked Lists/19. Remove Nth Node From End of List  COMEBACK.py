# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return head
        else:
            length = 0
            counter = 0
            count = curr = tail = head
            while count:
                count = count.next
                length += 1
            if n >= length:
                return head.next
            while counter < length - n - 1 and tail:
                tail = tail.next
                counter += 1
            tail.next = tail.next.next
            return curr     
                
                