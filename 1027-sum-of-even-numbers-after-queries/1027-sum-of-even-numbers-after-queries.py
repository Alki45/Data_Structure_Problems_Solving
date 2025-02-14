class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        result = []
        even_sum = sum(num for num in nums if num % 2 == 0)
        for i in queries:
            index=i[1]
            val=i[0]
            if(nums[index]%2==0):
                even_sum-=nums[index]
            nums[index]+=val
            if(nums[index]%2==0):
                even_sum+=nums[index]
            result.append(even_sum)
        return result