class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        def helper(left, right):
            if left == right:
                return nums[left]
            pick_left = nums[left] - helper(left + 1, right)
            pick_right = nums[right] - helper(left, right - 1)
            return max(pick_left, pick_right)
        
        return helper(0, len(nums) - 1) >= 0