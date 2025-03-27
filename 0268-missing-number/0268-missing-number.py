class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        dict_num={num:num for num in range(len(nums)+1)}
        nums.sort()
        new_list=[num for num in dict_num.values()]
        return (list(set(new_list) - set(nums))[0])

        