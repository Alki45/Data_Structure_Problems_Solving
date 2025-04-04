class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        initial=1
        for i in range(1,len(nums)):
            if(nums[i]!=nums[i-1]):
                nums[initial]=nums[i]
                initial+=1
        return initial

        
        