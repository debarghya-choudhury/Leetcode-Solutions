class Solution:
    def reverse(self, x: int) -> int:
        x = str(x)
        sign = ""
        ans = ""
        if x[0] == "-":
            sign = x[0]
            x = x[1:len(x)]
        for i in range(0, len(x)):
            ans = x[i] + ans
        ans = int(sign + ans)
        return ans if ans >= -2**31 and ans <= 2**31 - 1 else 0