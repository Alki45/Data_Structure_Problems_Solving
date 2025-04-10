class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        S_ptr=0
        T_ptr=0
        count=0
        while(S_ptr<len(s) and T_ptr<len(t)):
            if(s[S_ptr]==t[T_ptr]):
                count+=1
                T_ptr+=1
                S_ptr+=1
            else:
                S_ptr+=1


        return (len(t)-count)
        