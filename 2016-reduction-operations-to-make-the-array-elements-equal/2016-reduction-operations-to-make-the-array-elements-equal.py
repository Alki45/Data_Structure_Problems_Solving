class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        nums.sort()
        operation=0
        count=0
        for i in range(1,len(nums)):
            if(nums[i]!=nums[i-1]):
                count+=1
            operation+=count
        return operation

        