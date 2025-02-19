class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        result = [''] * len(s)  
        for i, key in enumerate(indices):
            result[key] = s[i]
        return ''.join(result)