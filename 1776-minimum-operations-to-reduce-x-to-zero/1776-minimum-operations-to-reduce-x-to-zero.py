class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        left=0
        target=sum(nums)-x
        total=0
        result=float('inf')
        for i in range(len(nums)):
            total+=nums[i]
            while(total>target and left<=i):
                total-=nums[left]
                left+=1
            if(total==target):
                result=min(result,len(nums)-(i-left+1))
                
        
        if(result==float('inf')):
            return -1
        return result
        
            