class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        def Max_Pick(left, right):
            if left == right:
                return nums[left]

            pick_left = nums[left] - Max_Pick(left + 1, right)
            pick_right = nums[right] - Max_Pick(left, right - 1)
            return max(pick_left, pick_right)
        
        return Max_Pick(0, len(nums) - 1) >= 0