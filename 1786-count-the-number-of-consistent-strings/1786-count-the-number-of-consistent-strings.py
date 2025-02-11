class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        count=0
        for i in words:
            Len_char=0
            for j in i:
                if(j in allowed):
                    Len_char+=1
                else:
                    break
            if(Len_char==len(i)):
                count+=1
        return count

        