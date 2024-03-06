# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # I thought values are distinct
        # new_dict = {}
        # pos = 0
        # while head:
        #     if not head.val in new_dict:
        #         new_dict[head.val] = pos
        #         pos += 1
        #     else:
        #         return True
        #     head = head.next
        # return False

        # slow and fast pointer concept
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
