class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        Distict_list=set(nums)
        if(len(nums)==len(Distict_list)):
            return False
        return True
        