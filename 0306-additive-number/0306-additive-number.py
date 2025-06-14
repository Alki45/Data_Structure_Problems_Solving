class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        n = len(num)
        
        # Try all possible splits for the first and second number
        for i in range(1, n):
            for j in range(i + 1, n):
                num1, num2 = num[:i], num[i:j]
                
                # Skip if num1 or num2 has leading zeros
                if (len(num1) > 1 and num1[0] == '0') or (len(num2) > 1 and num2[0] == '0'):
                    continue
                # Start building the additive sequence
                while j < n:
                    sum_str = str(int(num1) + int(num2))
                    if not num.startswith(sum_str, j):
                        break
                    j += len(sum_str)
                    num1, num2 = num2, sum_str
                
                # If we've consumed the whole string, it's valid
                if j == n:
                    return True
        
        return False