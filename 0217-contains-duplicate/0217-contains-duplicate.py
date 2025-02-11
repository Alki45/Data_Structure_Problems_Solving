from collections import Counter
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums_dic=Counter(nums)
        if(max(nums_dic.values())>1):
            return True
        return False

        