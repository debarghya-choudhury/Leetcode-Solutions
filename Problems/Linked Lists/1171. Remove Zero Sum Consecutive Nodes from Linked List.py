# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # Brute force Solution
        
        h = dummy = ListNode(-1)
        dummy.next = head
        p1 = head

        while p1:
            print("p1.val", p1.val)
            print("h.val", h.val)
            sum = 0
            p2 = p1
            while p2:
                print("p2.val", p2.val)
                sum += p2.val
                print("sum", sum)
                if sum == 0:
                    h.next = p2.next
                    p1 = h.next
                    break
                else:
                    p2 = p2.next
            if sum != 0:
                p1 = p1.next
                h = h.next
        
        return dummy.next