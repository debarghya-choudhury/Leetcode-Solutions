class Solution:
    def addBinary(self, a: str, b: str) -> str:
        num = self.binToDec(a) + self.binToDec(b)  # without any methods
        ans = self.decToBin(str(num))
        return str(ans)

    def binToDec(self, val: str):
        sum = 0
        x = len(val)-1
        for i in range(0 , len(val)):
            sum = sum + ( int(val[i]) * 2**x )  
            x -= 1
        return sum

    def decToBin(self, val: str):
        val = int(val)
        ans = ""
        if val != 1 and val != 0:
            rem = val % 2
            ans = str(rem)
            val = val // 2
            while 2 <= val:
                rem = val % 2
                ans = str(rem) + ans
                val = val // 2
            ans = str(val) + ans    
        else:
            return val
        return ans        

