class Solution:
    def splitString(self, s: str,  prev: int = None) -> bool:
        if prev is not None:
            if not s:
                return True
            for i in range(1, len(s) + 1):
                num = int(s[:i])
                if num == prev - 1 and self.splitString(s[i:], num):
                    return True
            return False
        else:
            for i in range(1, len(s)):
                num = int(s[:i])
                if self.splitString(s[i:], num):
                    return True
            return False