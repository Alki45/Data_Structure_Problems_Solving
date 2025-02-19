class Solution:
    def isHappy(self, n: int) -> bool:
        Calculated = set()
        
        while n != 1 and n not in Calculated:
            Calculated.add(n)
            n=[int(digit) ** 2 for digit in str(n)]
            n = sum(n)
            
        return n == 1