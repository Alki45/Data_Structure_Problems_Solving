class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        l,r=0,0
        g.sort()
        s.sort()
        result=0
        while (l<len(g) and r<len(s)):
            if(s[r]>=g[l]):
                result+=1
                l+=1
                r+=1
            else:
                r+=1
        return result