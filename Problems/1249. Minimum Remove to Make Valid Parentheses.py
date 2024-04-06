class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        ans = ""
        stack = []
        counter = 0
        removalArr = []
        for i in range(len(s)):
            # print(stack)
            ans += s[i]
            # print(ans)
            if s[i] == "(":
                stack.append([s[i],i])
            elif s[i] == ")":
                if len(stack) > 0 and stack[-1][0] == "(":
                    stack.pop()
                else:
                    ans = ans[:-1]
                    counter += 1
        
        for arr in stack:
            arr[1] = arr[1] - counter
            removalArr.append(arr[1])

        remSetIndex = set(removalArr)
        solution = ""
        
        for j in range(len(ans)):
            if j not in remSetIndex:
                solution += ans[j]
        # print(stack)
        return solution