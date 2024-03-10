# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        # for i in range(1, n + 1):       #  O(n^2)
        #     if isBadVersion(i):
        #         return i
        i = 1
        while i <= n:                     #  O(log n)
            mid = (i + n) // 2
            if isBadVersion(mid):
                if isBadVersion(mid - 1) == True and i <= (mid - 1) <= n:
                    n = mid - 1     
                else:
                    return mid
            elif not isBadVersion(mid):
                i = mid + 1 
        
        return mid