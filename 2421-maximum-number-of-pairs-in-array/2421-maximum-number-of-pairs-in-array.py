from collections import Counter
class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        result = [0, 0]
        freq_nums = Counter(nums)
        for key, value in freq_nums.items():
            result[0] += value // 2 
            result[1] += value % 2 
        return result


        