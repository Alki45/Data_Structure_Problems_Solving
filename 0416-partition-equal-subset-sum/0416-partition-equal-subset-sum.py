class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        set_element=set([0])
        total = sum(nums)
        if total % 2 != 0:
            return False
        target = total // 2
        for num in nums:
            new_sum = set()
            for element in set_element:
                if num + element == target:

                    return True
                else:
                    new_sum.add (num + element)
            set_element.update(new_sum)
        return target in set_element




        