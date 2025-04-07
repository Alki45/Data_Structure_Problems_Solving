class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        index=0
        count=0
        Char_count={"a":0,"b":0,"c":0}
        for i in range(len(s)):
            Char_count[s[i]]+=1

            while Char_count['a']>0 and Char_count['b']>0 and Char_count['c']>0:
                count+=len(s)-i
                Char_count[s[index]]-=1
                index+=1
        return count



        