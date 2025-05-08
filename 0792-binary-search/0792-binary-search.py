class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1

        while left <= right:
            midd = left + ((right - left)//2)
            if nums[midd] == target :
                return midd
            elif nums[midd] > target :
                right = midd -1
            else:
                left = midd + 1
        return  -1