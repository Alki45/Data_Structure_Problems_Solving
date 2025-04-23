class Solution:
    def removeStars(self, s: str) -> str:
        strs=list(s)
        stack=[]
        l=0
        n=len(strs)
        while l<n:
            while (l<n and strs[l].isalpha()):
                stack.append(strs[l])
                l+=1
            if(l<n and strs[l]=='*'):
                stack.pop()
                l+=1
            else:
                l+=1
        return "".join(stack)