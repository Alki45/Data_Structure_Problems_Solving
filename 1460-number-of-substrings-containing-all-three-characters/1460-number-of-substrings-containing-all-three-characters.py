class Solution:
        def numberOfSubstrings(self, s: str) -> int:
            res = 0
            n = len(s) 
            l = 0
            uniqueChars = set()
            while l < (n - 2):
                r = l
                while r < n:
                    uniqueChars.add(s[r])
                    r += 1
                    if len(uniqueChars) == 3:
                        res += 1
                uniqueChars.clear()    
                l += 1
            
            
            return res



        