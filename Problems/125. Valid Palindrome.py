class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.strip()
        string = ""
        for i in s:
            if i.isalnum():
                string += i.lower()
        s = string
        print(s)
        L = 0                                           # O(n)
        R = len(s) - 1

        while L <= R:
            if s[L] != s[R]:
                return False
            L += 1
            R -= 1
        
        return True