from collections import Counter
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        fre_nums=Counter(nums)
        result=[]
        for key,value in fre_nums.items():
            if(value==2):
                result.append(key)
        return result        