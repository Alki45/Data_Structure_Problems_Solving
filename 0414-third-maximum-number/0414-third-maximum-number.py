class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        
        nums=list(set(nums))
        nums.sort()
        if(len(nums)>=3):
            for i in range(2):
                nums.pop()
        return max(nums)
        