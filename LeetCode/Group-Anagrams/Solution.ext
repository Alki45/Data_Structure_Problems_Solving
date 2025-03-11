class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups={}
        for i in range(len(strs)):
            stri=tuple(sorted(strs[i]))
            if(stri not in groups):
                groups[stri]=[strs[i]]
            else:
                groups[stri].append(strs[i])
        result=[value for key,value in groups.items() ]
        return result