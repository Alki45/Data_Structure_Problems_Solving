class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        left=0
        right=len(nums)-1
        count=0
        while(left<right and right<len(nums)):
            if(nums[left]+nums[right]==k):
                count+=1
                left+=1
                right-=1
            elif(nums[left]+nums[right]>k):
                right-=1
            else:
                left+=1
        return count

        