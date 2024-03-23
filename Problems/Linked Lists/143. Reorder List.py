# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head:
            return
        if not head.next:
            return
        flag = True
        slow = fast = l = r = x = y = head
        c = count = loopCount = 0
        d = 0
        while fast and fast.next:
            d = fast.next
            fast = fast.next.next
            slow = slow.next
            count += 1
        m = revM = mid = slow 
        # print(m.val)
        if fast != None:   # odd
            r = fast
            flag = False
        else:              # even
            r = d
        if flag == False:
            last = mid.next
        loopCount = count
        # print(r)
        # print(loopCount)
        revP = mid.next
        while revP:
            # print("revP", revP)
            # print("revM", revM)
            holdP = revP.next
            holdM = revP
            if revM == mid:
                revM.next = None
            revP.next = revM
            revM = holdM
            revP = holdP
        # print("r.next", r.next)
        holdL = 0
        while c < loopCount:
            # print("l", l.val)
            # print("r", r)
            holdL = l.next
            holdR = r.next
            # print("holdR", holdR)
            # print("holdL", holdL)
            l.next = r
            r.next = holdL if holdL != mid else None
            l = holdL
            r = holdR
            # print("r", r)
            c += 1
        if flag == False:
            last.next = mid

