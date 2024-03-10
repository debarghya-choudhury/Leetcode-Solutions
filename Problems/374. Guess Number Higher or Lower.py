# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        l = 1
        r = n

        while l <= r:                #O(n)
            mid = (l + r) // 2
            cond = guess(mid)
            if cond == -1:   # left
                r = mid - 1
            elif cond == 1: # right
                l = mid + 1
            else:
                return mid
        return -1

                