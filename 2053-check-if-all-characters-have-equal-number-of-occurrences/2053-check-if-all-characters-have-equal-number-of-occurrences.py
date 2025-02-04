class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        dict={}
        for i in s:
            if(i in dict):
                dict[i]+=1
            else:
                dict[i]=1
        uniq_val={value: key for key,value in dict.items()}
        uniq_dictionary={value:key for key,value in uniq_val.items()}
        return (len(uniq_dictionary)==1)