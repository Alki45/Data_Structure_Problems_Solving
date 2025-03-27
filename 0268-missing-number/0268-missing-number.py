class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        new_list=[num for num in range(len(nums)+1)]
        return (list(set(new_list) - set(nums))[0])

        