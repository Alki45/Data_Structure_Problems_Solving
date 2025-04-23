class Solution:
    def clearDigits(self, s: str) -> str:
        strs=list(s)
        l=0


        while l<len(strs):
            if(strs[l].isdigit()):
                strs.pop(l)
                strs.pop(l-1)
                l-=1
            else:
                l+=1
        return "".join(strs)

        