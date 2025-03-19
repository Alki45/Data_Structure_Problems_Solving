class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_, largestCount = 0, 0
        arr = collections.Counter()
        for idx in range(len(s)):
            arr[s[idx]] += 1
            largestCount = max(largestCount, arr[s[idx]])
            if max_ - largestCount >= k:
                arr[s[idx - max_]] -= 1
            else:
                max_ += 1
        return max_
        