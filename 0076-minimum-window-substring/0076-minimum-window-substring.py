class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""
        t_count = Counter(t)
        window = {}
        have, need = 0, len(t_count)
        left = 0
        res = ""
        min_len = float("inf")

        for right in range(len(s)):
            c = s[right]
            window[c] = window.get(c, 0) + 1


            if c in t_count and window[c] == t_count[c]:
                have += 1
            while have == need:
                if (right - left + 1) < min_len:
                    res = s[left:right+1]
                    min_len = right - left + 1

                window[s[left]] -= 1
                if s[left] in t_count and window[s[left]] < t_count[s[left]]:
                    have -= 1
                left += 1

        return res
