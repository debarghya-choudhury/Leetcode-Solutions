class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {
            '(' : ")",
            '{' : "}",
            '[' : "]"
        }

        stack = []

        for i in range(0, len(s)):
            if s[i] in brackets:  # open bracket
                stack.append(s[i])
            else:                 # close bracket
                if len(stack) == 0 or brackets[stack[-1]] != s[i]:
                    return False
                else:
                    stack.pop()
        if len(stack): 
            return False
        else:
            return True     

        # failed attempts below :- 
        
        # for i in range(1, len(s)):
        #     if(ord(s[i]) == ord(s[i-1]) + 1 or ord(s[i]) == ord(s[i-1]) + 2):
        #         return True
        #     else:
        #         return False    

        # brackets_map = {
        #     '(' : ")",
        #     '{' : "}",
        #     '[' : "]"
        # }

        # for i in range(0, len(s)):
        #     if s[i] in brackets_map:
        #         rest_set = set(s[i+1:len(s)])
        #         if brackets_map[s[i]] in rest_set:
        #             return True
        #         else:
        #             return False    
                

