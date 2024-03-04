class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = 0
        x = 1
        ans = []
        for i in range(len(digits)-1, -1, -1):
            num = num + (digits[i] * x)
            x *= 10

        num = str(num + 1)    

        for i in range(0, len(num)):
            ans.append(int(num[i]))

        return ans    