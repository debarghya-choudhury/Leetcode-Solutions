class Solution:                 # Using Recursion
    def makeGood(self, s: str) -> str:
        for i in range(len(s)-1):
            if s[i+1].isupper() and s[i] == s[i+1].lower():
                # print(s[:i] + s[i+2:])
                return self.makeGood(s[:i] + s[i+2:]) 
            elif s[i+1].islower() and s[i] == s[i+1].upper():
                return self.makeGood(s[:i] + s[i+2:]) 
        return s
