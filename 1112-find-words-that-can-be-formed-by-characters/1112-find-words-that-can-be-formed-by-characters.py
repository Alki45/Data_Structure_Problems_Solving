class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        result=0
        for i in words:
            count=0
            for j in i:
                if(j in chars and(i.count(j)<=chars.count(j))):
                    count+=1
            if(count==len(i)):
                result+=len(i)
        return result


        