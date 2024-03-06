# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        if len(lists) < 2:
            return lists[0]

        list1 = lists[0]
        list2 = lists[1]
        dummyNode = node = ListNode(-1)

        while list1 and list2:
            if list1.val < list2.val:
                node.next = list1
                list1 = list1.next

            else:
                node.next = list2
                list2 = list2.next
            node = node.next

        node.next = list1 or list2    
        
        return self.mergeKLists([dummyNode.next] + lists[2:])
        