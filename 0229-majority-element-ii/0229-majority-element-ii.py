from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        freq_num=Counter(nums)
        result=[]
        for key,value in freq_num.items():
            if(value> len(nums)//3):
                result.append(key)
        return result
        