class Solution:
    def minimumLength(self, s: str) -> int:
        i = 0
        j = len(s) - 1

        # O(n)
        while i < j:
            if s[i] == s[j]:
                if s[i+1] == s[i] and i+1 != j:
                    i += 1
                elif s[j-1] == s[i] and i+1 != j:
                    j -= 1
                else:
                    i += 1
                    j -= 1
            else:
                break

        print(s[i:j+1])
        print("i", i, s[i],"j", j, s[j])

        return (j+1) - i