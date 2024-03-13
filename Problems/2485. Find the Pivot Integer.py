class Solution:
    def pivotInteger(self, n: int) -> int:

        for i in range(1, n+1):         # O(n^2)  coz im dumb
            x = i
            suml = 0
            sumr = 0
            for j in range(1, x+1):
                suml += j
            for k in range(x, n+1):
                sumr += k
            if suml == sumr:
                return x
        return -1


