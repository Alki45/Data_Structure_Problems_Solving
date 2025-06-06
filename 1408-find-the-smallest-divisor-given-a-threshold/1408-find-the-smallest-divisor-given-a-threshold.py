class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        left, right = 1, max(nums)
        while left < right:
            mid = (left + right) // 2
            total = sum(math.ceil(num / mid) for num in nums)
            if total > threshold:
                left = mid + 1
            else:
                right = mid
        return left