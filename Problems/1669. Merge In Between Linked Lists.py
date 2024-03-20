# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        dummy = ListNode(-1)
        dummy.next = list1
        p3 = dummy
        p1 = p2 = list1

        count = 0
        while count < a and p1:
            count += 1
            p1 = p1.next
            p3 = p3.next

        count = 0
        while count <= b and p2:
            count += 1
            p2 = p2.next

        head2 = list2
        while head2.next:
            head2 = head2.next

        p3.next = list2
        head2.next = p2

        return list1