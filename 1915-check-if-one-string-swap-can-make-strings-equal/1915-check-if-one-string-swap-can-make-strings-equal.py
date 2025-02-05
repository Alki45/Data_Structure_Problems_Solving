class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        count=0
        if(len(s1)==len(s2)):
            for i in range(len(s1)):  
                if(sorted(s1)!=sorted(s2)):
                    return False
                elif(s1[i]!=s2[i]):
                    count+=1  

            if(count<=2):
                return True
        return False
        