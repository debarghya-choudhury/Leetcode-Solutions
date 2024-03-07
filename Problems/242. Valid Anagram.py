class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        if len(s) == 0 or len(t) == 0:
            return False
        
        map_s = {}

        for i in range(0, len(s)):
            if s[i] in map_s:
                map_s[s[i]] += 1
            else:
                map_s[s[i]] = 1  # count
        
        for i in range(0, len(t)):
            if t[i] in map_s:
                map_s[t[i]] -= 1
            else:
                return False

        for i in map_s:
            if map_s[i] > 0:
                return False
        
        return True
        