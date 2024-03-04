# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # curr = None
        # while head:
        #     hold = head.next
        #     head.next = curr
        #     curr = head
        #     head = hold 
        # return curr       

        # Two pointers
        # prev, curr = None, head
        # while curr:
        #     hold = curr.next
        #     curr.next = prev
        #     prev = curr
        #     curr = hold
        # return prev

        # recursive approach
        if not head:
            return None

        if head.next:
            newHead = self.reverseList(head.next)
            head.next.next = head 
        head.next = None
        return newHead
      


