class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        result=[i for i in range(len(nums)+1)]
        diff= list(set(result) - set(nums))
        for i in diff:
            return i
        