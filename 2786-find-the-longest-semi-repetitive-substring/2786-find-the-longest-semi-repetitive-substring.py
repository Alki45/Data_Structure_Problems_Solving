class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        start = 0
        max_len = 1
        adj_count = 0

        for end in range(1, len(s)):
            if s[end] == s[end - 1]:
                adj_count += 1

            while adj_count > 1:
                if s[start] == s[start + 1]:
                    adj_count -= 1
                start += 1

            max_len = max(max_len, end - start + 1)

        return max_len