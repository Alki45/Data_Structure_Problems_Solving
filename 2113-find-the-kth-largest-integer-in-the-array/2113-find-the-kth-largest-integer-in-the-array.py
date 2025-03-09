class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        result=[int(i) for i in nums]
        result.sort()
        for i in range(k-1):
            result.pop()
        return str(max(result))
        