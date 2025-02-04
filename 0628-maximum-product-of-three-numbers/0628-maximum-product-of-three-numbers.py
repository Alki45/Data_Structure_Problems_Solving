class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        Product=1
        nums.sort()
        If_Positive=nums[-1]*nums[-2]*nums[-3]
        If_Negative=max(nums[0]*nums[1]*nums[2],nums[0]*nums[1]*nums[-1])
        Product=max(If_Positive,If_Negative)

        return Product