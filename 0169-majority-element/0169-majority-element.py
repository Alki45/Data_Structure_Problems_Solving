from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        Dic_nums=Counter(nums)
        Max_mod=max(Dic_nums.values())
        for key,value in Dic_nums.items():
            if value ==Max_mod:
                return key
        