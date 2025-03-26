class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        prd=1
        nums.sort()
        if(len(nums)>=3):
            prd=max(nums[-1]*nums[-2]*nums[-3],nums[0]*nums[1]*nums[-1])
        return prd

        
        