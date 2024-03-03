class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        res = ""
        counter = 0  # to count how many 1s
        
        # or
        counterUsingMethod = s.count("1")  # leanind .count() method for strings
        
        for i in range(0, len(s)):
            if s[i] == "1":
                counter += 1
        if counter:
            res = "1"*(counter-1) + "0"*(len(s)-counter) + "1"
        else:
            return s
        return res