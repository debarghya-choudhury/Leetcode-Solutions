class Solution:
    def fib(self, n: int) -> int:
        if n == 2 or n == 1:        # O(2^n)
            return 1
        elif n == 0:
            return 0
        else:
            return self.fib(n-1) + self.fib(n-2)
        

        # better approach

        if n <= 1:                  # O(2^n)
            return n
        else:
            return self.fib(n-1) + self.fib(n-2)