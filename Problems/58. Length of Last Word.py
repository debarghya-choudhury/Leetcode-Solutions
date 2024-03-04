class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # arr = s.split()                       # with method
        # print(arr)
        # return len(arr[-1])

        ans = 0                                 # without method
        flag = False
        if s:
            for i in range(len(s)-1, -1, -1):
                if s[i] != " ":
                    ans += 1
                    flag = True
                elif flag == True:
                    break
        return ans    