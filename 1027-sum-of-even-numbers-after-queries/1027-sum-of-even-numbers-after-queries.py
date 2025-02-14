class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        result = []
        even_sum = sum(num for num in nums if num % 2 == 0)
        
        for val, index in queries:
            current_val = nums[index]
            new_val = current_val + val
            if current_val % 2 == 0:
                even_sum -= current_val
            nums[index] = new_val
            if new_val % 2 == 0:
                even_sum += new_val  
            result.append(even_sum)
        return result