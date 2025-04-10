class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left=0
        total=0
        Min_=float("inf")
        for right in range(len(nums)):
            total+=nums[right]
            while(total>=target):
                Min_=min(right-left+1,Min_)
                total-=nums[left]
                left+=1
        if(Min_==float("inf")):
            return 0
        return Min_

        
        