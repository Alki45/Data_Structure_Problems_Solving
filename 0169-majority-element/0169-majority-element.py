class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority_elemnt=[]
        nums_set=set(nums)
        for i in nums_set:
            majority_elemnt.append(nums.count(i))
        for i in nums_set:
            if(max(majority_elemnt)==nums.count(i)):
                return i
        return 0
            
        