class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        New_nums=set([x for x in range(len(nums)+1)])
        missing_num=list(New_nums - set(nums))
        for i in missing_num:
            return i
        