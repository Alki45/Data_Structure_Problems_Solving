class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort()
        largest = nums[-k]
        return largest
        