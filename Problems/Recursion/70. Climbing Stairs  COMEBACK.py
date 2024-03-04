class Solution:
    def climbStairs(self, n: int) -> int:
    # Recursive approach   O(2^n)
    #    if n == 0:     
    #        return 1
    #    elif n > 0 and n <= 3:
    #        return n
    #    else:
    #        return self.climbStairs(n-1) + self.climbStairs(n-2) 

    # loop approach     O(n)
       if n == 0:
            return 1
       elif n > 0 and n <= 3:
            return n
       else:
            n1, n2 = 2,3
            for i in range(3, n):
                hold = n1 + n2
                n1 = n2
                n2 = hold
            return n2 

    