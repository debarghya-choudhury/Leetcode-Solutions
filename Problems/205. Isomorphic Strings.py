class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hMap1 = {}
        hMap2 = {}
        for i in range(len(s)):
            if ( s[i] in hMap1 and t[i] != hMap1[s[i]] ) or t[i] in hMap2 and s[i] != hMap2[t[i]]:
                return False
            hMap1[s[i]] = t[i]
            hMap2[t[i]] = s[i]
            
        return True

