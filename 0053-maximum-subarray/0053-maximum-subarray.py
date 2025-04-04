class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = float('-inf')
        current_sum = 0
        for num in nums:
            current_sum=current_sum + num
            current_sum=max(num,current_sum)
            max_sum = max(max_sum,current_sum)
        return max_sum
        