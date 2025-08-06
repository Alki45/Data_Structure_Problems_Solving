class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}

        def recursion (i, current_sum):
            if (i,current_sum) in memo:
                return memo[(i,current_sum)]

            if i == len(nums):
                if current_sum == target:
                    return 1
                else:
                    return 0
            else:
                memo[(i,current_sum)] = (recursion(i+1, current_sum + nums[i]) + recursion(i + 1,current_sum - nums[i]))
            return memo [(i,current_sum)]

        return recursion (0,0)
        

        