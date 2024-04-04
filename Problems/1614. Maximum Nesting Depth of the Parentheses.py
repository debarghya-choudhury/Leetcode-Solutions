class Solution:
    def maxDepth(self, s: str) -> int:
        ans = 0
        depth = 0
        stack = []
        for i in s:
            if i == "(":
                depth += 1
                stack.append(i)
                ans = max(ans, depth)
            elif i == ")":
                if len(stack) and stack[-1] == "(":
                    depth -= 1
                    stack.pop()
        return ans
            