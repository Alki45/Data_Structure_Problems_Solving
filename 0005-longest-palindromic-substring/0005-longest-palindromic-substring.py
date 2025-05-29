class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        max_len = 0
        result = ""

        for i in range(n):
            for j in range(i, n):
                substring = s[i:j+1]
                if substring == substring[::-1] and len(substring) > max_len:
                    max_len = len(substring)
                    result = substring

        return result