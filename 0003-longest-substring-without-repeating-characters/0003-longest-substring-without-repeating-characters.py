class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
            l1 = []  
            max_length = 0  
            
            for char in s:
                if char in l1: 
                    while char in l1:
                        l1.pop(0)  
                l1.append(char) 
                max_length = max(max_length, len(l1))  
            
            return max_length