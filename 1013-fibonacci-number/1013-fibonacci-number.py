class Solution:

    def fib(self, n: int) -> int:
        memo = {}
        def mem(i):
            if i == 0 or i == 1:
                return i
            if i not in memo:
                memo[i] = mem(i-1) + mem(i-2)
            return memo[i]
        return mem(n)
            


            
        
        