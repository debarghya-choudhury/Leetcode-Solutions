## COMEBACK

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummyNode = node = ListNode(-1)
        while list1 and list2:
            if list1.val < list2.val:
                node.next = list1
                list1 = list1.next

            else:
                node.next = list2
                list2 = list2.next
            node = node.next

        # if list1:
        #     node.next = list1
        # elif list2:
        #     node.next = list2

        node.next = list1 or list2

        return dummyNode.next        


########   REVISIT
    
    # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        p1 = list1
        p2 = list2
        head = dummy = ListNode(-1)
        # O(m + n)
        while p1 and p2:
            if p1.val < p2.val:
                dummy.next = p1
                temp = p1.next
                p1.next = None
                p1 = temp
                dummy = dummy.next
            elif p2.val < p1.val:
                dummy.next = p2
                temp = p2.next
                p2.next = None
                p2 = temp
                dummy = dummy.next
            elif p1.val == p2.val:
                temp1 = p1.next
                temp2 = p2.next
                p1.next = p2
                p2.next = None
                dummy.next = p1
                p1 = temp1
                p2 = temp2
                dummy = dummy.next.next
            else:
                break
            print(dummy.val)
        if p2:
            dummy.next = p2 
        if p1:
            dummy.next = p1 
        return head.next



            

        
            

        