class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0: return False

        s = str(x)                 # O(n)
        L = 0
        R = len(s) - 1

        while L <= R:
            if s[L] != s[R]:
                return False
            L += 1
            R -= 1
        
        return True